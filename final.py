      # -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:33:48 2021

@author: modis
"""

import numpy as np
import cv2
import os
from annoy import AnnoyIndex

sift = cv2.SIFT.create()

bf = cv2.BFMatcher()

clusters = 50

PATH = 'new/'
QUERY_IMAGE_PATH = '60.png'

descriptors = []

for (dirpath, dirnames, filenames) in os.walk(PATH):
    for filename in filenames:
        img = cv2.imread(PATH + filename, 0)
        kp, des = sift.detectAndCompute(img, None)
        if des is not None:
            descriptors.extend(des)
    descriptors = np.float32(descriptors)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 5, .01)
    centroids = cv2.kmeans(descriptors, clusters, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
    centroids = centroids[2]
    for i, centroid in enumerate(centroids):
        counter_sum = np.sum(centroid)
        centroids[i] = [float(n)/counter_sum for n in centroid]

histograms = []
for (dirpath, dirnames, filenames) in os.walk(PATH):
    	for filename in filenames:
            img = cv2.imread(PATH + filename, 0)
            counter = np.zeros((clusters,), dtype=np.uint32)
            try:
                kp, d = sift.detectAndCompute(img, None)
            except Exception as e:
                print(str(e))
                continue
            
            if d is None:
                continue
            
            for i, des in enumerate(d):
                counter_sum = np.sum(des)
                d[i] = [float(n)/counter_sum for n in des]
            
            matches = bf.knnMatch(d, centroids, k=2)
            
            for match, k in matches:
                counter[match.trainIdx] += 1
            counter_sum = np.sum(counter)
            counter = [float(n)/counter_sum for n in counter]
            histograms.append({'frame':int(filename.replace('.png', '').replace('test', '')), 'count': counter})

t = AnnoyIndex(clusters, 'angular')
for histogram in histograms:
    t.add_item(histogram['frame'], histogram['count'])
t.build(10)

img1 = cv2.imread(QUERY_IMAGE_PATH, 0)
kp1, des1 = sift.detectAndCompute(img1, None)
for i, des in enumerate(des1):
    counter_sum = np.sum(des)
    des1[i] = [float(n)/counter_sum for n in des]

matches = bf.knnMatch(des1, centroids, k=2)
counter = np.zeros((clusters,), dtype=np.uint32)
for match in matches:
    counter[match[0].trainIdx] += 1     

counter_sum = np.sum(counter)
counter = [float(n)/counter_sum for n in counter]

nn = t.get_nns_by_vector(counter, 9, include_distances = True)

neighbors = nn[0]
distances = nn[1]

for i, neighbor in enumerate(neighbors):
    	print("Frame ID: {}".format(neighbor))           
                