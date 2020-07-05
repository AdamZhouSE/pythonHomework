import collections
import heapq
s=input()
s=s[1:len(s)-1].split(",")
count=collections.Counter(s)
q=[]
res=""
for item in count.items():
    q.append([-item[1],item[0]])
heapq.heapify(q)
pre=None
while q or pre:
    if q:
        cur=heapq.heappop(q)
        res+=cur[1]
        cur[0]+=1
        if cur[0]==0:
            cur=None
    else:
        cur=None
    if pre:
        heapq.heappush(q,pre)
    pre=cur
print(list(map(int,list(res))))
