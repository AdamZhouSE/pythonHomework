import heapq
class node:
    def __init__(self,c=0,t=0):
        self.c=c
        self.t=t
    def __lt__(self,t):
        return self.c<t.c

num=list(map(int, input().strip().split(' ')))
n=num[0]
k=num[1]
c=list(map(int, input().strip().split(' ')))
h=[]
sum1=0
t=[]
for i in range(n):
    t.append(node(-c[i],i+1))
res=[0 for i in range(n)]
num=0
for i in range(0,n):
    j=num
    while (j<i+k+1)&(j<n):
        heapq.heappush(h,t[j])
        num+=1
        j+=1
    temp=heapq.heappop(h)
    res[temp.t-1]=i+k+1
    sum1-=temp.c*(i+k+1-temp.t)
print(sum1)
for i in range(n):
    print(res[i],end=' ')