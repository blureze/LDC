# -*- coding: utf-8 -*-

topic_dict = {}
with open('topic.txt', 'r') as f:
	for line in f:
		tmp = line.split(',')
		for item in tmp:
			ttmp = item.split(":")
			topic_num = ttmp[0]
			filename = ttmp[1].split("'")[1]
			topic_dict[topic_num] = filename
f.closed

for k,v in topic_dict.items():
	content = []
	with open("./train/" + v + ".txt", 'r', encoding='GBK') as f:
		for line in f:
			if line != '\n' and line != ('# ' + v + '\n'):
				content.append(line)
		divide = int(len(content) / 3)
		
		partI = content[divide: divide+10]
		wf = open("./output/" + v + "_1.txt", "ab")
		for item in partI:
			wf.write(item.encode('utf-8'))
		wf.closed

		partII = content[2*divide: 2*divide+10]
		wf = open("./output/" + v + "_2.txt", "ab")
		for item in partII:
			wf.write(item.encode('utf-8'))
		wf.closed
	f.closed