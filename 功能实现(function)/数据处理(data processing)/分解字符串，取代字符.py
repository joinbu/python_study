
A = 'abc'

for i in A:
	print(i)


#拓展

#取代单类字符，用X取代字符串中的a字符
A = 'abc'
for i in A:
	if i == 'a':
	 	A = A.replace(i,"X")
print(A)

#取代某些字符，用X取代字符串中的ab字符
A = 'abc'
B = 'ab'

for i in A:
	if i in B:
	 	A = A.replace(i,"X")
print(A)
