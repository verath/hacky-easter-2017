import os
import re
from PIL import Image

# sqrt(1600) == 40
IMG_PER_ROW = 40
SHARD_SIZE = 12

glued_img = Image.new('RGBA', (IMG_PER_ROW * SHARD_SIZE, IMG_PER_ROW * SHARD_SIZE))

def fname_key(fname):
	match = re.match(r'img_\d+_(.*?)_\d+_(.*?)\.png', fname)
	g1 = match.group(1)
	g2 = match.group(2)
	# Sort upper case after lower case
	if g1.isupper(): g1 = "~" + g1
	# Add leading 0
	if len(g2) == 1: g2 = "0" + g2
	return g1 + g2

for i, filename in enumerate(filenames):
	y_offset = (i // IMG_PER_ROW) * SHARD_SIZE
	x_offset = (i % IMG_PER_ROW) * SHARD_SIZE

	im = Image.open('shards/' + filename)
	glued_img.paste(im, (x_offset, y_offset))

glued_img.save('glue.png')
