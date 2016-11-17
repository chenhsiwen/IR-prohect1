#encoding=utf-8
import sys
import jieba
import tool 

reload(sys)
sys.setdefaultencoding('utf-8')

Query = open('queries.txt', 'r').read()
Doc = open('document.txt', 'r')
Jieba = open('Jieba.txt', 'w')
dicttionary = open('mydict.txt', 'w')

#input the query 
querieslist = []
queries = []
querie = []
term = [] 
termstr = ''
Query = Query.decode('utf8')
Query = Query.replace('。', '')
Query = Query.replace('）', '，')
Query = Query.replace('（', '，')
Query = Query.replace(', ', '，')
Query = Query.replace('，， ', '，')
Query = Query.replace('．', '，')
#for ch in xrange(0x41, 0x5B): 
#	ch = unichr(ch)	
#	Query = Query.replace(ch, '')
#for ch in xrange(0x61, 0x7B): 
#	ch = unichr(ch)	
#	Query = Query.replace(ch, '')

for i in range(len(Query)):
	if Query[i] == "\n" :
		termstr = ''.join(term) 
		term = []
		querie.append(termstr)
		queries.append(querie)
		querie = []
		querieslist.append(queries)
		queries = []
	else :
		if Query[i] == "\t" :
			termstr = ''.join(term) 
			term = []	
			querie.append(termstr)
			queries.append(querie)
			querie = []
		else :
			if Query[i] == "，" :
				termstr = ''.join(term) 
				term = []	
				querie.append(termstr)
			else:
				term.append(Query[i])

#input the doc
documentlist = []
temp = Doc.readline()
i=0
while temp != '':
	temp=Doc.readline()
	documentlist.append(temp)
	i += 1

#build the dicttionary from our query to improve the jeiba performance
for i in range(len(querieslist)):
	for j in range(2):
		for k in range(len(querieslist[i][2*j+1])):
			dicttionary.write(querieslist[i][2*j+1][k])
			dicttionary.write(' 10\n')
dicttionary.close();

#cut the sentense to the word
jieba.load_userdict("mydict.txt")
for i in range(len(querieslist)):
	words = jieba.cut(querieslist[i][2][0], cut_all=False)
	for word in words:
		Jieba.write(word)
		Jieba.write(' ')
	Jieba.write("\n")
Jieba.close() 
for i in range(len(querieslist)):
	querieslist[i][2] = [] 
Jieba = open('Jieba.txt', 'r')
i = 0 
temp = Jieba.readline()
while temp != '':
	temp = temp.replace('\n', '')
	for j in range(len(temp)):
		if temp[j] == " " :
			termstr = ''.join(term) 
			term = []	
			querieslist[i][2].append(termstr)
		else:
			term.append(temp[j])
	i+=1
	temp = Jieba.readline()

#weighting term
for i in range(len(querieslist)) :
	for j in range(len(querieslist[i])) :
		for k in range(len(querieslist[i][j])) :
			if j == 1: 
				querieslist[i][j][k] = [querieslist[i][j][k] , 3 ]
			else :
				querieslist[i][j][k] = [querieslist[i][j][k] , 1 ]
			querieslist[i][j][k][0] = querieslist[i][j][k][0].decode('utf8')
#combine query
for i in range(len(querieslist)) :
	Q4 = [] 
	
	for k in range(len(querieslist[i][2])) :
		if len(querieslist[i][2][k][0]) > 2 :
			Q4.append(querieslist[i][2][k])
	Q4 = tool.combinequery(Q4, querieslist[i][1])
	Q4 = tool.combinequery(Q4, querieslist[i][3])
	querieslist[i].append(Q4)
count = 0
for i in range(len(querieslist)) :
	print i
	for j in range(4,5) :
		for k in range(len(querieslist[i][j])) :
			print querieslist[i][j][k][1]
			print querieslist[i][j][k][0]
			count +=1
