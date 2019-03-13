

import json
import re
import jieba.analyse as analyse


f = open("Chat_7152a8c3643915cb465599ed75f5de7a.json",'r',encoding='utf-8')
data = json.load(f)
f.close()

# extract message
ignore = ['w','<']
text = ''
for message in data:
    if message["Message"][0] in ignore:
        continue
    text += message['Message'].strip()+' '

# load stop words
with  open("stop_words.txt", 'r', encoding = 'gbk') as f:
    while True:
        word = f.readline().strip()
        if word:
            ignore.append(word)
        else:
            break
print(ignore)

#extract key words
tfidf = analyse.extract_tags
f = open("topK.txt",'w',encoding='gbk')
keyword = ''
keywords = tfidf(text, topK=200)
for i, word in enumerate(keywords):
    if word not in ignore:
        keyword += word + ' '
print(keyword)
f.write(keyword)
f.close()



