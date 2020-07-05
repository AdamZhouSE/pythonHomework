import collections
import heapq
s=input()
s=s[1:len(s)-1].split(",")
count=collections.Counter(s)
q=[]
for item in count.items():
    q.append([item[1],item[0]])
heapq.heapify(q)
print(heapq.heappop(q)[1])
