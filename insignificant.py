# Mitchell Vitez, 6/10/15

"""
Insignificant Bits - Hides text messages in green pixels of images
"""

from PIL import Image
import sys

MAX_MESSAGE_CHARS = 1000
MAX_MESSAGE_BITS = 8 * MAX_MESSAGE_CHARS

def isEven(num):
	return num % 2 == 0

def getBit(pixel):
	if isEven(pixel[1]):
		return 0
	return 1

def getBitsFromImage(img, imgPix):
	bits = []
	for x in xrange(img.size[0]):
		for y in xrange(img.size[1]):
			bits.append(getBit(imgPix[x, y]))
			if len(bits) > MAX_MESSAGE_BITS:
				return bits
	return bits

def findMessage(filename):
	img = Image.open(filename)
	imgPix = img.load()

	bits = getBitsFromImage(img, imgPix)

	chars = []
	for bit in xrange(len(bits) / 8):
		byte = bits[bit * 8 : (bit + 1) * 8]
		chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))

	return ''.join(chars)

# We hide one bit per pixel, information density could be much higher
# 1 bit means odd green pixel, 0 bit means even green pixel
def transformPixel(pixel, bit):
	green = pixel[1]
	newGreen = green
	if green is 0:
		newGreen = int(bit)
	elif isEven(green) and bit is '1':
		newGreen = green - 1
	elif not isEven(green) and bit is '0':
		newGreen = green - 1
	pixelAsList = list(pixel)
	pixelAsList[1] = newGreen
	return tuple(pixelAsList)

def insertMessage(filename, message):
	old = Image.open(filename)
	new = Image.new(old.mode, old.size, None)
	
	oldPix = old.load()
	newPix = new.load()

	binaryMessage = ''.join(format(ord(char), '08b') for char in message)
	messagePos = 0

	for x in xrange(old.size[0]):
		for y in xrange(old.size[1]):
			if messagePos >= len(binaryMessage):
				newPix[x, y] = oldPix[x, y]
			else:
				newPix[x, y] = transformPixel(oldPix[x, y], binaryMessage[messagePos])
				messagePos += 1
	return new

if __name__ == '__main__':
	filename = raw_input().strip('\r')
	message = findMessage(filename)
	for char in message:
		if char.isalpha() or char == ' ':
			sys.stdout.write(char)

	# filename = "files/insignificant.png"
	# new = insertMessage(filename, "YOUR MESSAGE HERE")
	# new.save("files/insignificant2.png")
