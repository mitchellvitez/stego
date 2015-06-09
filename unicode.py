# -*- coding: utf-8 -*-
# Does steganography on a message by using similar-looking unicode characters
# Mitchell Vitez, 6/8/15

alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
	desteggedMessage = []
	for char in message:
		if ord(char) > END_OF_ASCII:
			desteggedMessage.append(char)
		else:
			pass # ignore chars that are already ascii
	return ''.join(desteggedMessage)

if __name__ == '__main__':
	message = raw_input('What is your message? ')
	print 'Destegged message is: ' + desteg(message)
