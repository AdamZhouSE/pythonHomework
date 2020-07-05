import re
list=input()
pattern=re.compile("\d+")
A=pattern.findall(list)
for i in range(len(A)):
	A[i]=int(A[i])
N=int(len(A)**0.5)
numpy=[]
for i in range(N):
	line=[]
	for j in range(N):
		line.append(A[i*N+j])
	numpy.append(line)
print(max(A))