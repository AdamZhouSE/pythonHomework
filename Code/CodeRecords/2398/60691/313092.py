import queue
N = 1000+5
n,t_max = 0,0
cow = [0]*N
def check(x):
    dance = queue.PriorityQueue()
    for i in range(1,x+1):
        dance.put(cow[i])
    for i in range(1,n+1):
        cur = dance.get()
        dance.put(cur+cow[i])
    cur = 0
    while(not dance.empty()):
        cur = dance.get()
    return cur<=t_max
n,t_max = map(int,input().split())
for i in range(1,n+1):
    cow[i] = int(input())
l,r = 0,n+1
while l+1<r:
    mid = l + ((r-1)>>1)
    if check(mid):
        r = mid
    else:
        l = mid
print(r)
