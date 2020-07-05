import re
list=input()
pattern=re.compile("\-\d+|\d+")
A=pattern.findall(list)
for i in range(len(A)):
	A[i]=int(A[i])

if A==sorted(A,reverse=True):
	result=0
elif A==sorted(A):
	result=len(A)-1
else:
	for i in range(1,len(A)-1):
		l = sorted(A[0:i])
		r = sorted(A[i+1:len(A)],reverse=True)
		if A[0:i]==l and A[i+1:len(A)]==r and l[i-1]<A[i]and A[i]>r[0]:
			result=i
			break
print(result)