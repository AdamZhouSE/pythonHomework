import re
sea=re.compile(r'\d+')

def find(M,N,i,j):
    if i==len(M):
        return 0
    elif j==len(N):
        return 0
    else:
        if M[i] == N[j]:
            return 1 + find(M, N, i + 1, j + 1)
        else:
            return 0
    

N=sea.findall(input())
M=sea.findall(input())
L=0
for i in range(len(N)-L):
    for j in range(len(N)-L):
        count=0
        count=find(M,N,i,j)
        if count>L:
            L=count
print(L)