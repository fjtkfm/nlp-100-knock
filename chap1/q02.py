# coding: utf-8

word1 = 'パトカー'
word2 = 'タクシー'

word = ''
for i in range(0, len(word1)):
	word += word1[i]
	word += word2[i]
print(word)
