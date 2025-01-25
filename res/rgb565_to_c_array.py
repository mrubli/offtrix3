#!/usr/bin/env python3

import os
import re
import struct
import sys

# Check if the file name is provided as an argument
if len(sys.argv) < 2:
	print("Usage: python rgb565_to_c_array.py <input_file>")
	sys.exit(1)

# Get the file name from the first argument
input_file = sys.argv[1]

# Read the binary file
with open(input_file, 'rb') as f:
	data = f.read()

# Convert binary data to 16-bit integers (words)
words = struct.unpack('>64H', data)

# Generate C-style array
base_name = os.path.splitext(os.path.basename(input_file))[0]
base_name = re.sub(r'[^a-zA-Z0-9_]', '_', base_name)
c_array = f"const uint16_t image_{base_name}[64] = {{\n"
for i, word in enumerate(words):
	if i % 8 == 0:
		c_array += "\t"
	c_array += f"0x{word:04X},"
	if (i + 1) % 8 == 0:
		c_array += "\n"
	else:
		c_array += " "
c_array += "};"

# Print the C-style array to stdout
print(c_array)
