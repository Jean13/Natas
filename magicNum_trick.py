#!/usr/bin/python

import sys

# Tricks programs into believing a certain file is another kind of file.
# For magic numbers, see: 
# http://www.astro.keele.ac.uk/oldusers/rno/Computing/File_magic.html


# Image formats
JPEG = '\xFF\xD8\xFF\xE0'
GIF = '\x47\x49\x46\x38'
PNG = '\x89\x50\x4e\x47'
BMP = '\x42\x4d'

# Compression formats
ZIP = '\x50\x4b\x03\x04'
GZ = '\x1f\x8b'
BZ = '\x42\x5a'

# Archive formats
TAR = '\x75\x73\x74\x61\x72'


def main():
	if len(sys.argv[1:]) != 3:
		print "magicNum_trick.py: Trick a program into believing your code " \
		"is another kind of file."
		print "\nUsage: ./magicNum_trick.py <number of file to cloak as> " \
				"<filename to save as> <code file> \n"

		print '''Formats:
		
		1 - JPEG
		2 - GIF
		3 - PNG
		4 - BMP
		5 - ZIP
		6 - GZ
		7 - BZ
		8 - TAR
		'''

		sys.exit(0)

	# Original input
	form = sys.argv[1]
	filename = sys.argv[2]
	c0de = sys.argv[3]
	with open(c0de, 'r') as f:
		code = f.read()

	# The real format - modify accordingly
	trick = open(filename, 'w')

	# Conversion
	if form == '1' or 'JPEG':
		trick.write(JPEG + code)

	elif form == '2' or 'GIF':
		trick.write(GIF + code)

	elif form == '3' or 'PNG':
		trick.write(PNG + code)

	elif form == '4' or 'BMP':
		trick.write(BMP + code)
	
	elif form == '5' or 'ZIP':
		trick.write(ZIP + code)

	elif form == '6' or 'GZ':
		trick.write(GZ + code)

	elif form == '7' or 'BZ':
		trick.write(BZ + code)

	elif form == '8' or 'TAR':
		trick.write(TAR + code)

	trick.close

main()

