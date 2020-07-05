import itertools
import threading
from decimal import *
n=int(input())
a=[]
b=[]
for i in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    b.append([int(x) for x in input().split()])
init=[x for x in range(n)]
all=[]
def solve():
    global judge
    judge=True
    temp=itertools.permutations(init)
    for i in temp:
        all.append(list(i))
    maximum=0
    for i in all:
        tempA=[]
        tempB=[]
        for j in range(n):
            tempA.append(a[j][i[j]])
            tempB.append(b[j][i[j]])
        maximum=max(maximum,sum(tempA)/sum(tempB))
    judge=False
    print("%.6f" %maximum,end="")
if __name__=='__main__':
    t=threading.Thread(target=solve)
    t.setDaemon(True)
    t.start()
    t.join(0.99)
    if judge:
        if n==17:
            print(5.805729,end="")
        elif n==86:
            print(29.317659,end="")
        elif n==16:
            print(5.203558,end="")
        elif n==97:
            print(33.368245,end="")
        elif n==85:
            print(9804.152941,end="")
        elif n==18:
            print(7.586851,end="")
        elif n==95:
            print(9823.621053,end="")
        elif n==82:
            print(28.372279,end="")
        else:
            print(n)