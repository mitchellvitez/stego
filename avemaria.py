# Mitchell Vitez, 6/9/15

"""
Ave Maria Cipher - Converts messages to Latin exultations
"""

import random

PERCENT_NOUNS = .30 # * 100 to get actual percentage

nouns = { "a":"Deus",
		"b":"Creator",
		"c":"Conditor",
		"d":"Opifex",
		"e":"Dominus",
		"f":"Dominator",
		"g":"Confolator",
		"h":"Arbiter",
		"i":"Iudex",
		"k":"Illuminator",
		"l":"Illustrator",
		"m":"Rector",
		"n":"Rex",
		"o":"Imperator",
		"p":"Gubernator",
		"q":"Factor",
		"r":"Fabricator",
		"s":"Conseruator",
		"t":"Redemptor",
		"v":"Auctor",
		"x":"Princeps",
		"y":"Pastor",
		"z":"Moderator" }

reverse_nouns = dict(reversed(item) for item in nouns.items())

adjectives = { "a":"clemens",
		"b":"clementibimus",
		"c":"pius",
		"d":"pibimus",
		"e":"magnus",
		"f":"excelsus",
		"g":"maximus",
		"h":"optimus",
		"i":"sapientibimus",
		"k":"inuisibilis",
		"l":"immortalis",
		"m":"aeternus",
		"n":"semperiternus",
		"o":"gloriosus",
		"p":"fortisimus",
		"q":"sanctibimus",
		"r":"incompraehensibilis",
		"s":"omnipotens",
		"t":"pacificus",
		"v":"misericors",
		"x":"misericordibimus",
		"y":"cunctipotens",
		"z":"magnificus" }

reverse_adjectives = dict(reversed(item) for item in adjectives.items())

def decodePrayer(message):
	letters = []
	for word in message.split(' '):
		if word.endswith(','):
			word = word[:-1]
		letters.append(reverse_nouns.get(word, ''))
		letters.append(reverse_adjectives.get(word, ''))
	return ''.join(letters)

def encodePrayer(message):
	words = []
	isNoun = True
	for letter in message:
		letter = letter.lower()
		if letter.isalpha():
			if isNoun:
				words.append(nouns[letter])
			else:
				words.append(adjectives[letter])
				words.append(',')
			words.append(' ')
			isNoun = random.random() < PERCENT_NOUNS
	return ''.join(words)

if __name__ == '__main__':
	import fileinput
	for message in fileinput.input():
		print decodePrayer(message)
