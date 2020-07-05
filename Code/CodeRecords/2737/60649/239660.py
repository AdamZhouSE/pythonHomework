import collections
import heapq
s=input()
n=len(s)
s=s[1:len(s)-1].split(",")
count=collections.Counter(s)
q=[]
for item in count.items():
    q.append([-item[1],item[0]])
res=""
while q:
    tmp=heapq.heappop(q)
    if(-tmp[0]>(len(s)//3)):
        res+=tmp[1]
    else:
        break
print(list(map(int,list(res))))
