# -*- coding: utf-8 -*-

vowels = ['а','и','і','ї','е','є','о','у','ь','ю','я']
consonants = {
				1 : ['б','п'],
				2 : ['в','ф'],
				3 : ['г','ґ','к','х'],
				4 : ['д','т'],
				5 : ['ж','ч','ш','щ'],
				6 : ['з','с','ц'],
				7 : ['й','л'],
				8 : ['м','н'],
				9 : ['р']
			}
letterCode = {}

def Normalization():
	for keys in consonants.keys():
		for items in consonants[keys]:
			items = items.decode('utf-8')
			letterCode[items] = keys

Normalization()
