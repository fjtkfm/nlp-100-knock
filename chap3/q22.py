import json
import re

england_article = ''
with open('jawiki-country.json') as jawiki_country_json:
	jp_wiki = json.load(jawiki_country_json)
	for article in jp_wiki:
		if article['title'] == 'イギリス':
			england_article = article['text']
			break

pattern = r'イギリス'
matchedList = re.findall(pattern, england_article)
if matchedList:
	print(len(matchedList))
