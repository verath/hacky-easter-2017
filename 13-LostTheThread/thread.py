from PIL import Image

im = Image.open("thread.png")
width, height = im.size
pix = im.load()

# The image contains morse-code representations of
# 0s and 1s. Find these by looking for black pixels
# separated by at least 2 white pixels
segments = []
currSegment = ""
for x in range(1, width):
	(_, _, _, prevA) = pix[x-1, 1]
	(_, _, _, currA) = pix[x, 1]
	prevBlack = (prevA == 255)
	currBlack = (currA == 255)
	
	# 2 white in a row, create a new segment
	if (not currBlack) and (not prevBlack):
		if currSegment:
			segments.append(currSegment)
			currSegment = ""
		continue

	if prevBlack:
		currSegment += "1"
	elif currSegment:
		currSegment += "0"

# Transform the morse code to binary
binary = ""
for seg in segments:
	if seg == "111111111111111":
		binary += "0"
	elif seg == "10111111111111":
		binary += "1"
	else:
		print("Unknown segment:", seg)

# The binary number is 841 char long, sqrt(841) == 29, 
# so probably 29x29 qr-code
outIm = Image.new("1", (29, 29))
outIm.putdata([int(x) for x in binary])
outIm.save("out.png")

# Scan the out.png, to find the password for the level:
# kiwisarekewl
