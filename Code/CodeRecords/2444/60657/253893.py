import re
A=input()
for i in range(len(A)-1):
    if A[i]=='[':
        for k in range(i+1,len(A)):
            if A[k]==']':
                cons=A[i+1:k]
                end=k
                break
A=A[k+2:]
new=re.findall(r'[\d]',A)
k=new[0]
t=new[1]
cons=cons.split(',')
cons=[int(x) for x in cons]
def cal(A,j,t):
    for i in range(len(A)-1):
        for k in range(i+1,len(A)):
            if abs(int(A[i])-int(A[k]))<=int(t) and abs(i-k)<=int(j):
                
                return 'true'
    return 'false'
print(cal(cons,k,t))
