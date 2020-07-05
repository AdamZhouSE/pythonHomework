n=int(input())
t=list(map(int,input().split(' ')))
q=[]
t.sort()
q.append(t.pop(0))
while len(t)>0:
    r=t.pop(0)
    if r>=sum(q):
        q.append(r)
print(len(q))