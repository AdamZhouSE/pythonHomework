t=int(input())
for i in range(t):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    maxcount=1
    for j in range(n):
        count=1
        for k in range(n):
            if l1[j]>l1[k] and l1[j]<l2[k]:
                count+=1
        if count>maxcount:
            maxcount=count
        count=1
        for k in range(n):
            if l2[j]>l1[k] and l2[j]<l2[k]:
                count+=1
        if count>maxcount:
            maxcount=count
    print(maxcount)