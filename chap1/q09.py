import random


def sort_word_randomly(target):
	if len(word) < 5:
		return target
	middle_part = list(word[1:-1])
	random.shuffle(middle_part)
	return target[0] + ''.join(middle_part) + target[-1]


before = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
after = []
for word in before.split(' '):
	after.append(sort_word_randomly(word))
print(' '.join(after))
