# -*- coding: utf-8 -*-

from uaLanguage import vowels
from uaLanguage import letterCode
import re

def Soundex(word):
	if len(word) == 0:
		return '00000'
	word = word.decode('utf-8').lower()
	word = re.sub('[%s]' % ''.join(vowels).decode('utf-8'), '', word)
	result = [letterCode[word[0]],0,0,0,0]
	word = word[1:]
	i = 1
	for letter in word:
		charCode = letterCode[letter]
		if charCode != result[i - 1]:
			result[i] = charCode
			i = i + 1
		if i == 5:
			break
	return int(''.join(str(x) for x in result))
