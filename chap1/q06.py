def make_char_n_gram(target, n):
	result = []
	for index in range(len(target)):
		word = target[index:index + n]
		if len(word) < n:
			word += ' ' * (n - len(word))
		result.append(word)
	return result

word1 = 'paraparaparadise'
X = make_char_n_gram(word1, 2)
word2 = 'paragraph'
Y = make_char_n_gram(word2, 2)

add = set()
for char in X:
	if char in add:
		continue
	add.add(char)
for char in Y:
	if char in add:
		continue
	add.add(char)

bi = set()
minus = set()
for char in X:
	if char in Y:
		bi.add(char)
	else:
		minus.add(char)
for char in Y:
	if char in X:
		bi.add(char)
	else:
		minus.add(char)

print(add)
print(bi)
print(minus)
