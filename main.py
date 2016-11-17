#encoding=utf-8
import Inputlayer
import tool
import sys
import math
from operator import itemgetter

reload(sys)
sys.setdefaultencoding('utf-8')


querieslist = Inputlayer.querieslist
documentlist = Inputlayer.documentlist

num_doc = len(documentlist)
num_query = len(querieslist)

method = 4

ranklist = [] 

for q in range(num_query):
	query = querieslist[q][method]
	num_term = len(query)
	weight = [] 
	col = [] 
	idf = [] 
	rank = [] 
	print 'do0'
	#check whther there is a term i in doc j or not
	for j in range(num_term) :
		print query[j][0]
		idf.append(0)
		for i in range(num_doc) :
			tf = tool.chinese_find(query[j][0],documentlist[i])
			col.append(tf)
			if tf != 0 :
				idf[j] += 1  
		if idf[j] > 0 :
			idf[j]= math.log(num_doc/idf[j],2)	
		weight.append(col)
		col = []
	print 'do1'
	#build the weight matrix
	for i in range(num_term) :
		for j in range(num_doc) :
			if weight[i][j] != 0 :
				weight[i][j] = math.log(1+weight[i][j],2) * idf[i] * query[i][1]
			else :
				weight[i][j] = 0  
	print 'do2'
	#calculate the rank
	for i in range(num_doc):
		product = 0
		dist = 0
		for j in range(num_term):
			product += weight[j][i]*idf[j]
			dist += math.pow(weight[j][i],2)
		if product != 0 :
			rank.append([i,product/math.sqrt(dist)])
		else :
			rank.append([i,0])
	print 'do3'
	rank = sorted(rank, key=itemgetter(1), reverse=True)
	for i in range(10):
		print rank[i][0]
		print rank[i][1]
		print documentlist[rank[i][0]]
	ranklist.append(rank)	







