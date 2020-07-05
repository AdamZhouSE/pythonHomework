import re
list=input()
pattern=re.compile("\-\d+|\d+")
A=pattern.findall(list)
for i in range(len(A)):
	A[i]=int(A[i])
k=int(input())

if k in A:
	print(A.index(k))
else:
	print(-1)