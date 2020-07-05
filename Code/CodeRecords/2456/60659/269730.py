import re
list1 = input()
pattern = re.compile('\-\d+|\d+')
A = pattern.findall(list1)
for i in range(len(A)):
	A[i]=int(A[i])
counts=[]
for i in range(len(A)-1):
	counter=0
	for j in range(i+1,len(A)):
		if A[j]<A[i]:
			counter+=1
	counts.append(counter)
counts.append(0)
print(counts)