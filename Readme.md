We both are from India and India has a lot of monuments, and it gets very tough to know where it is located. So, we thought of implementing something that tells us where the monument is located just by providing an image to the code. 

## What it does
The user enters an image of the monument, and the locator shows similar images and it's location on the map. 

## How we built it
We have used python language for making the locator using OpenCV library and some machine learning as well as deep learning concepts. We used reverse image matching to get a higher accuracy and SIFT, which is used for feature matching in the images. We also did data pre-processing to not make the program run again and again on the same data, which took around 30 minutes.

## Challenges we ran into
Firstly, There is no such dataset present on the internet for all the monument images, which was challenging for us to create it as the data needed to be scraped from the internet from different sites and made it into a single format, which was very time-consuming. Furthermore, the program was taking 30 seconds to show the results, which is not a good sign and needed to be optimized. We worked a lot in optimizing the results and reduced the 30 seconds down to 0.3 seconds for getting the similar monuments images.

## Accomplishments that we're proud of
We are proud to make it a very fast similar image generating system within 1 second to get the results and proud of developing the entire system which is a big project in very less time.

## What we learned
It was a lot of learning throughout the event as we learned the reverse image match to increase the accuracy. Also, we learned about integrating maps with the algorithm that we developed for the multiple image matching and connecting the latitude and longitude for it.

## What's next for Monument Locator
We are planning to expand the dataset and get as many images as possible. So we plan to automate the process by building a pipe that would automatically store the location details of any monument via search results on the database directly, reducing efforts to manage it manually.