#encoding=utf-8

import sys
import math
reload(sys)
sys.setdefaultencoding('utf-8')

def chinese_find(query, doc ):
	doc = doc.decode('utf8')
	query = query.decode('utf8')
	count = 0 
	k = 3
	if len(query)== 0 :
		return 0
	for i in range(len(doc)-len(query)):
		if doc[i] == '\t':
			k -= 1 
		btn = 0
		for j in range(len(query)):
			if (doc[i+j] == query [j]):
				btn = k
			else :
				btn = 0
				break
		count += btn
	return count*math.log(len(query)+1,2)
def combinequery(Q1, Q2):
	for l in range(len(Q2)):
		token = -1 
		for j in range(len(Q1)):
			if Q1[j][0]  == Q2[l][0] :
				token = j
				break 
		if token != -1:
			Q1[j][1] +=  Q2[l][1] 
		else :
			Q1.append(Q2[l])
	return Q1
