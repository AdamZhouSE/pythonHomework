from heapq import *

k,m = [int(x) for x in input().split()]
heap = [1]
cnt = 0
ans1 = ""
while cnt<k:
    top= heappop(heap)
    heappush(heap,2*top+1)
    heappush(heap,4*top+5)
    ans1+=str(top)
    cnt+=1
print(ans1)
l , r , max_ = 0,m,0
ans2 = ""
while l<=r and r<len(ans1):
    for i in range(l,r+1):
        if int(ans1[i])>max_:
            max_=int(ans1[i])
            l = i+1
    ans2+=str(max_)
    r+=1
    max_=0
print(ans2,end="")