def make_char_n_gram(target, n):
	result = []
	for index in range(len(target)):
		word = target[index:index + n]
		if len(word) < n:
			word += ' ' * (n - len(word))
		result.append(word)
	return result


def make_word_n_gram(target, n):
	result = []
	target = target.replace(',', '').replace('.', '')
	words = target.split(' ')
	for index in range(len(words)):
		word_list = []
		for i in range(index, index + n):
			try:
				word_list.append(words[i])
			except IndexError:
				word_list.append('')
		result.append(word_list)
	return result

sentence = "I am an NLPer"
print(make_char_n_gram(sentence, 2))
print(make_word_n_gram(sentence, 2))
