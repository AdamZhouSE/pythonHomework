import re
list1 = input()
pattern = re.compile('\-\d+|\d+')
A = pattern.findall(list1)
for i in range(len(A)):
	A[i]=int(A[i])
lower=int(input())
upper=int(input())
counter=0
num=[]
for i in range(len(A)):
	count=0
	for j in range(i,len(A)):
		count+=A[j]
		num.append(count)

for i in num:
	if lower<=i<=upper:
		counter+=1
print(counter)