import collections
str1=input()
str1=str1.replace('[','')
str1=str1.replace(']','')
list1=str1.split(',')
A=[]
for i in range(len(list1)):
    A.append(int(list1[i]))
K=int(input())
N = len(A)
P = [0]
for x in A:
    P.append(P[-1] + x)      
ans = N+1 
monoq = collections.deque()
for y, Py in enumerate(P):
    while monoq and Py <= P[monoq[-1]]:
        monoq.pop()
    while monoq and Py - P[monoq[0]] >= K:
        ans = min(ans, y - monoq.popleft())
    monoq.append(y)
if ans < N+1:
    print(ans)
else:
    print(-1)
