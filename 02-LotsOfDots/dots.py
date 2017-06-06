from PIL import Image

im = Image.open("dots.png")
rgb_im = im.convert('RGB')
pix = rgb_im.load()

colors = {}
width, height = rgb_im.size
for x in range(width):
	for y in range(height):
		c = pix[x, y]
		
		#if c not in colors:
		#	colors[c] = 0
		#colors[c] += 1

		# (232, 178, 97) is the most common non-white color.
		if c == (232, 178, 97):
			pix[x, y] = (255, 255, 255)

#for c in colors:
#	print(c, colors[c])

rgb_im.save("out.png")
