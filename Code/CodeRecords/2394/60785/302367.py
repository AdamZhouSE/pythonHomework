t=int(input())
for ii in range(t):
    n=int(input())
    num=[int(i) for i in input().split()]
    res=[]
    count=0
    for i in num:
        if i==0:count+=1
        else:res.append(i)
    res=res+count*[0]
    sli=num=[str(i) for i in res]
    print(' '.join(sli),end=' ')
    print()