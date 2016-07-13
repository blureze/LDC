from collections import defaultdict
import random

topic = defaultdict(list)
with open('calldata-train.txt', 'r', encoding='UTF-8') as f:
	for line in f:
		tmp = line.split('\t')
		filename = tmp[0]
		if filename == 'Filename':	continue
		topic_num = tmp[11].split('\n')[0]
		topic[topic_num].append(filename)
f.closed

# randomly select
final_topic = {}
for k,v in topic.items():
	length = len(v)
	index = random.randint(0, length-1)
	final_topic[k] = v[index]

# final_topic = sorted(final_topic)
print(final_topic)