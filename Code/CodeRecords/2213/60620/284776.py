n,m,q=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
for i in range(q):
    begin,end,first,second=map(int,input().split())
    index=0
    judge=0
    for j in range(m):
        if(first in a[j]):
            index=j
    if(begin-1<=index<=end-1):
        for k in range(index,end):
            if(second in a[k]):
                judge=1
    if(judge==0):
        print('No')
    else:
        print('Yes')