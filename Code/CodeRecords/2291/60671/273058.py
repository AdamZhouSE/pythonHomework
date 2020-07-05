from queue import PriorityQueue

q = PriorityQueue(maxsize=0)
length=int(input())
list0=input().split()
listnum=[]
for c in list0:
    listnum.append(int(c))
    
for i in listnum:
    q.put(i)
ans=0
while(q.qsize()>1):
    x=q.get()
    y=q.get()
    q.put(x+y)
    ans+=x+y

print(ans)


