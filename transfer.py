# -*- coding：utf-8 -*-
from langconv import *

def transfer(filename):
	with open("./output/" + filename +".txt", 'r', encoding='utf-8') as f:
		# wf = open(filename + "_trans.txt", "ab")
		for line in f:
			line = line.split(" ")
			content = ""
			for item in line[2:]:
				if(item == line[2]):
					content += item
				else:
					content += " " + item
			
			# 轉換簡體到繁體
			content = Converter('zh-hant').convert(content)
			# line = line.encode('utf-8')
			
			# wf.write(content.encode('utf-8'))
		# wf.closed 
	f.closed
	return content
		