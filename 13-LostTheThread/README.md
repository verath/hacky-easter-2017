# 13 - Lost the Thread

> Searching for eggs is fun! But sometimes they come in weird shapes and sizes. Download the image and wind up the strand!

We are also given an image:

![thread](thread.png)

Looking at the image, it looks like it is morse code of 1s and 0s. It turns
out that there are 841 such morse codes, making it likely that they encode
a 29x29 large qr-code. Indeed, after running [thread.py](thread.py) to 
transforms the morse codes -> binary -> a 29x29 image (where 0 = black, 1= white)
we get the solution qr-code:

![out](out.png)

