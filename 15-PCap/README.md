# 15 P Cap

We are provided with a packet capture file, `cap.pcapng`. Opening it in wireshark we can see that it is fairly large. After some investigating we find some SMB queries. Using wireshark it is easy to extract objects transfered over SMB (File -> Export Ebjects -> SMB).

Doing so we find an image called R05h4L.jpg, with a stick figure in it. But no egg. However, opening the image in a hex viewer we can see that towards the bottom there is a filename "imnothere.txt". Strange. 

Investigating further, we can see that the actual .jpg image data does not cover the entire file, instead a .zip file is embedded towards the end. Using 7-zip, it is possible to open R05h4L.jpg as a zip. We then find that it contains a file called "imnothere.txt". 

"imnothere.txt" does not look like a text file, so we try opening it as an image, which does indeed work. The image contains "7061n.php", which we can assume is a URL on the hacky easter server. Finally, https://hackyeaster.hacking-lab.com/hackyeaster/7061n.php gives us the egg. 
