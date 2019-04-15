# -*- coding: utf-8 -*-
import jieba

txt = open("doc.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
stop = open("stopwords.txt", "r", encoding='utf-8').read()
stopwords = jieba.lcut(stop)
counts = {}

for word in words:
    if word in stopwords:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(len(items)):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))

