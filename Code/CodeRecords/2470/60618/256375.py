T=int(input())
n=[]
A=[[0]*int(n**0.5)]*n
for i in range(0,T):
    n.append(int(input()))
    for j in range(0,n[i]**2):
        