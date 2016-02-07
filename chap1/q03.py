# coding: utf-8

sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
sentence = sentence.replace(',', '').replace('.', '')

wordCountList = []
for word in sentence.split(' '):
	wordCountList.append(len(word))
print(wordCountList)
