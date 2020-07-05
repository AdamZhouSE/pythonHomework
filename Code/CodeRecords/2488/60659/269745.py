import re
list1 = input()
pattern = re.compile('\-\d+|\d+')
A = pattern.findall(list1)
for i in range(len(A)):
	A[i]=int(A[i])
res=sorted(A)
counter=1
if len(A)>=3:
	while counter<len(A):
		res[counter],res[counter+1]=res[counter+1],res[counter]
		counter+=2
print(res)