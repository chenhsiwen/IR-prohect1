#encoding=utf-8
import main
import csv
import sys

sys.setdefaultencoding('utf-8')
reload(sys)
Doclist = open('doclist.txt', 'w')

querieslist = main.querieslist
documentlist = main.documentlist
ranklist = main.ranklist
num_query = len(querieslist)
method = 4

temp = []
IDliststr =''
IDlist = [] 
IDstr = ''
CHAR =[]
for q in range(num_query):
	Doclist.write(q)
	for j in range(10000):
		doc_id = ranklist[q][j][0]
		Doclist.write(doc_id)
		Doclist.write(' ')
	Doclist.write('\n')
Doclist.close();
#build the rel new list for top 100
col  = ['Id', 'Rel_News']  
IDlist.append(col)
for q in range(num_query):
	for j in range(100):
		doc_id = ranklist[q][j][0]
		for i in range(len(documentlist[doc_id])):
			if documentlist[doc_id][i] == "\t" :
				CHAR.append(' ')
				break
			else:
				CHAR.append(documentlist[doc_id][i])
	IDstr = ''.join(CHAR) 
	CHAR = []
	IDlist.append([q+1,IDstr])
	temp=[]


output = open("test10.csv","w")
w = csv.writer(output)
w.writerows(IDlist)
output.close()