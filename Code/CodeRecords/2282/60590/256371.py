t=int(input())
for _ in range(t):
    n=int(input())
    ins=input().split(' ');ins=[int(x) for x in ins]
    try:
        outs=input().split(' ');outs=[int(x) for x in outs]
    except Exception as e:
        del outs[3]
        outs=[int(x) for x in outs]
    max=0;count=0
    for i in range(n):
        start=0;
        if i!=0:
            start=outs[i-1]
            count-=1
        for j in range(i,n):
            if start<=ins[j]<=outs[i]:
                count+=1
        if count>max:
            max=count
    print(max)