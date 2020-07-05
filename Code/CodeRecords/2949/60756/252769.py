s=input().split()
del s[-1]
L=len(s)
s0=[]
for i in range(L):
    s0.append(s.pop())
print(' '.join(s0),end=' ')