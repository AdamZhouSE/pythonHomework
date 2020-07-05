import re
from fractions import Fraction
list=input()
pattern=re.compile("\-\d+|\d+")
A=pattern.findall(list)
for i in range(len(A)):
	A[i]=int(A[i])
k=int(input())

counts=[]
for i in range(len(A)):
	for j in range(i+1,len(A)):
		counts.append(Fraction(A[i],A[j]))
counts.sort()
res=counts[k-1]
result=[0,0]
result[0]=res.numerator
result[1]=res.denominator
print(result)