
def cipher(target):
	result = ''
	for char in target:
		result += chr(219 - ord(char)) if char.islower() else char
	return result

sentence = "Atbash is a simple substitution cipher for the Hebrew alphabet."

print(sentence)
sentence = cipher(sentence)
print(sentence)
sentence = cipher(sentence)
print(sentence)
