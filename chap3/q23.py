import json
import re

england_article = ''
with open('jawiki-country.json') as jawiki_country_json:
	jp_wiki = json.load(jawiki_country_json)
	for article in jp_wiki:
		if article['title'] == 'イギリス':
			england_article = article['text']
			break

# print(england_article)
sectionPattern = r'^=+'
for sentence in england_article.split('\n'):
	matchedSection = re.search(sectionPattern, sentence)
	if matchedSection:
		level = sentence.count('=') / 2 - 1
		print('%s : level %d' % (sentence, level))
