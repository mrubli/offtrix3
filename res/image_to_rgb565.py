#!/usr/bin/env python3

from PIL import Image
import sys
import os

def rgb888_to_rgb565(r, g, b):
	# Convert RGB888 to RGB565
	r5 = (r & 0xF8) >> 3
	g6 = (g & 0xFC) >> 2
	b5 = (b & 0xF8) >> 3

	# Combine into 16-bit value
	rgb565 = (r5 << 11) | (g6 << 5) | b5
	return rgb565

def convert_image_to_rgb565(input_path):
	# Get output path
	base_name = os.path.splitext(input_path)[0]
	output_path = base_name + '.raw'

	try:
		# Open and convert image to RGB
		img = Image.open(input_path)
		if img.mode != 'RGB':
			img = img.convert('RGB')

		width, height = img.size
		pixels = img.load()

		# Convert pixels and write to binary file
		with open(output_path, 'wb') as f:
			for y in range(height):
				for x in range(width):
					r, g, b = pixels[x, y]
					rgb565 = rgb888_to_rgb565(r, g, b)
					# Write as little-endian 16-bit value
					f.write(rgb565.to_bytes(2, byteorder='big'))

		print(f"Converted {input_path} to {output_path}")
		print(f"Image size: {width}x{height} pixels")

	except Exception as e:
		print(f"Error: {str(e)}")
		sys.exit(1)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python image_to_rgb565.py <image_file>")
		sys.exit(1)

	input_file = sys.argv[1]
	if not os.path.exists(input_file):
		print(f"Error: File {input_file} not found")
		sys.exit(1)

	convert_image_to_rgb565(input_file)
