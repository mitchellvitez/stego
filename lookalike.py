# -*- coding: utf-8 -*-
# Mitchell Vitez, 6/8/15

"""
Does steganography on a message by using similar-looking unicode characters
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
unicodeAlphabet = [u'\u0251', u'\u0185', u'\u010B', u'\u0257', u'\u0259',
				   u'\u0192', u'\u01E5', u'\u0127', u'\u0269', u'\u0237',
				   u'\u0138', u'\u026D', u'\u0271', u'\u0273', u'\u01A1',
				   u'\u01A5', u'\u01A3', u'\u0157', u'\u01A7', u'\u0165',
				   u'\u01DA', u'\u03BD', u'\u03E3', u'\u0436', u'\u045E',
				   u'\u0291']
END_OF_ASCII = 128

def unicodeToAscii(character):
	if character in unicodeAlphabet:
		return alphabet[unicodeAlphabet.index(character)]
	return ''

def asciiToUnicode(character):
	if character in alphabet:
		return unicodeAlphabet[alphabet.index(character)]
	return ''

def convertString(message, encodingFunc):
	message = message.lower()
	charList = []
	for char in message:
		charList.append(encodingFunc(char))
	return ''.join(charList)

def encode(message):
	return convertString(message, asciiToUnicode)

def decode(message):
	return convertString(message, unicodeToAscii)

def desteg(message):
	desteggedMessage = []
	for char in message:
		# ignore chars that are already ascii
		if ord(char) > END_OF_ASCII:
			desteggedMessage.append(char)
	return ''.join(desteggedMessage)

if __name__ == '__main__':
	import fileinput
	for message in fileinput.input():
		print desteg(message)

	# message = "YOUR MESSAGE HERE"
	# print encode(message)
