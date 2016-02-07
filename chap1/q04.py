# coding: utf-8

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
sentence = sentence.replace('.', '')

wordDict = {}
for index, word in enumerate(sentence.split(' ')):
	index += 1
	if index == 1 or index == 5 or index == 6 or index == 7 or index == 8 or index == 9 or index == 15 or index == 16 or index == 19:
		wordDict.setdefault(word[0], index)
	else:
		wordDict.setdefault(word[0:2], index)
print(wordDict)
