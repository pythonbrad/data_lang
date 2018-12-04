# -*- coding: utf-8 -*-
#buld_data by pythonbrad 28/04/2018
import json
import glob

word = {}
ext = '.lang'

for filename in glob.glob('*'+ext):
	lang = filename.split('.')[0]
	f=open(lang+ext, encoding='utf-8')
	data = f.read()
	f.close()
	data = data.splitlines()
	word_no_translate = []
	word_translate = []

	for i in data:
		if i != '':
			d = i.split('.')
			word_no_translate.append(d[0])
			word_translate.append(d[1])

	data = {'lang':{},'mlang':{}}

	for i in range(len(word_no_translate)):
	    data['lang'][i]=word_no_translate[i].capitalize()
	    data['mlang'][i]=word_translate[i].capitalize()

	word[lang] = data
	    
f=open('word.json', 'w')
json.dump(word, f)
f.close()

f=open('word.py', 'w', encoding='utf-8')
f.write("""# -*- coding: utf-8 -*-
dict_word = %s
"""%str(word))
f.close()