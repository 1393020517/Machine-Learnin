import jieba
import os
import codecs
import xlrd
import xlwt
import jieba
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
import sys


def eachFile(filepath):
    filelist = []
    pathDir = os.listdir(filepath)
    for s in pathDir:
        path='./聚类数据/'+s
        txt=open(path,'r',encoding='utf-8').read()
    for i in range(120):
            filelist.append(pathDir[i])
    return  filelist








def cut_word(text):
    readFile = open('./stopwords.txt','r',encoding='utf-8')
    stopWords = ['\n',]
    oneWords = readFile.readline()
    while oneWords:
        stopWords.append(oneWords.strip())
        oneWords = readFile.readline()
    wordList = list()
    for i in jieba.cut(text):
        if i not in stopWords:
            wordList.append(i)
    return" ".join(wordList)

def tfidf_print(textList,needWordNumber):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(textList))
    word = vectorizer.get_feature_names()
    weight = tfidf.toarray()
    wordDict = dict()
    weight = weight.T
    for i in range(len(weight)):
        wordDict[word[i]] = weight[i].sum()
    wordDict = sorted(wordDict.items(), key=lambda d:d[1], reverse = True)
    for i in range(needWordNumber):
        wordDict[i] = wordDict[i][0]
    print(wordDict[:needWordNumber])

def content(filepath):
    list=eachFile(filepath)
    content=[]

    for i in range(120):
        readFile = open('./聚类数据/'+list[i], 'r', encoding='utf-8').read()
        content.append(readFile)
    return content



def jvlei(K,fileName,needWordNumber):
    textList = list()
    for i in content(fileName):
        textList.append(cut_word(i))
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(textList))
    clf = KMeans(int(K))
    y_pred = clf.fit_predict(tfidf)
    flag = set(y_pred)
    result = dict()
    for i in flag:
        result[str(i)] = list()
    for i in range(len(y_pred)):
        result[str(y_pred[i])].append(textList[i])
    for i in result:
        tfidf_print(result[i],needWordNumber)



if __name__=='__main__':
    contents=content('./聚类数据/')

    textList = list()
    for i in contents:
        textList.append(cut_word(i))
    tfidf_print(textList,10)

    jvlei(120, './聚类数据/', 4)
