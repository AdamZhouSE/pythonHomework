import heapq
num=list(map(int, input().strip().split(' ')))
n=num[0]
k=num[1]
c=list(map(int, input().strip().split(' ')))
h=[]
sum1=0
res=[0 for i in range(k+n)]