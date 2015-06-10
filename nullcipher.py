# Mitchell Vitez, 6/9/15

"""
Null Cipher - Finds messages among lots of null characters
"""

def decode(message, rule):
	characterList = []
	words = message.split(' ')
	for word in words:
		characterList.append(rule(word))
	return ''.join(characterList)

# Below here are the rules to apply - ev
def firstCharInWord(word):
	return word[0]

N = 3
def nthCharInWord(word):
	return word[ N % len(word) ]

cycleCount = -1
def cycleThroughChars(word):
	global cycleCount
	cycleCount += 1
	return word[ cycleCount % len(word) ]

if __name__ == '__main__':
	import fileinput
	for message in fileinput.input():
		print decode(message, firstCharInWord)
 