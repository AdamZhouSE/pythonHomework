num=int(input())
for i in range(num):
    line1=list(map(int,input().split(' ')))
    size1=line1[0]
    size2=line1[1]
    sum=line1[2]
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    a.sort(reverse=True)
    b.sort(reverse=True)
    start1=0
    start2=0
    rt=[]
    while a[start1]>sum:
        start1+=1
    while b[start2]>sum:
        start2+=1
    for u in a[start1:]:
        for v in b[start2:]:
            if u+v==sum:
                rt.append(str(u)+' '+str(v))
    if len(rt)==0:
        print(-1)
    else:
        rt.reverse()
        for r in rt:
            print(r)
