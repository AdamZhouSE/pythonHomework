ans=[]
while True:
    s=input()
    if s=='-1':
        break
    if s=='2' and ans:
        ans.sort(key=lambda x:x[1])
        ans.pop()
    elif s=='3' and ans:
        ans.sort(key=lambda x:x[1])
        ans.pop(0)
    else:
        tmp=list(map(int,s.split()))
        co=[1 for i in ans if i[1]==tmp[2]]
        if not co:
            ans.append((tmp[1], tmp[2]))
bea=sum([i[0] for i in ans])
cost=sum([i[1] for i in ans])
print(bea,cost,end='')