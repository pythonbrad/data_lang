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
	data2 = {"themes":{}}
	theme_id = 0
	theme_name = ""
	theme = 0
	nb_word = 0
	for i in data:
		if "[THEME]" in i:
			theme = 1
			theme_name = i.replace("[THEME]", "")
			data2['themes'][theme_name] = {}
		elif i != '':
			d = i.split('.')
			if (not theme_name or nb_word > 10) and not theme:
				theme_name = "theme%s"%theme_id
				data2['themes'][theme_name] = {}
				theme_id += 1
				nb_word = 0
			data2['themes'][theme_name][d[0].capitalize()]=d[1].capitalize()
			nb_word += 1
	word[lang] = data2
f=open('word.json', 'w')
json.dump(word, f)
f.close()

f=open('word.py', 'w', encoding='utf-8')
f.write("""# -*- coding: utf-8 -*-
dict_word = %s
"""%str(word))
f.close()
