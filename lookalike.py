# -*- coding: utf-8 -*-
# Mitchell Vitez, 6/8/15

"""
Does steganography on a message by using similar-looking unicode characters
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
# TODO: Fill in the rest of the unicode alphabet
unicodeAlphabet = [u'\u212B', u'\u212C', u'\u2102']
END_OF_ASCII = 256

def unicodeToAscii(character):
	return alphabet[unicodeAlphabet.index(character)]

def asciiToUnicode(character):
	return unicodeAlphabet[alphabet.index(character)]

def convertString(message, steg):
	message = message.lower()
	charList = []
	for char in message:
		if steg:
			charList.append(asciiToUnicode(char))
		else:
			charList.append(unicodeToAscii(char))
	return ''.join(charList)

def encode(message):
	return convertString(message, True)

def decode(message):
	return convertString(message, False)

def desteg(message):
	message = unicode(message, 'utf-8')
	desteggedMessage = []
	for char in message:
		# ignore chars that are already ascii
		if ord(char) > END_OF_ASCII:
			desteggedMessage.append(char)
	return ''.join(desteggedMessage)

if __name__ == '__main__':
	message = raw_input('What is your message?\n')
	print 'Destegged message is: ' + desteg(message)
