k=int(input())
for qqq in range(0,k):
    n=int(input())
    num=list(map(int,input().split()))
    num.sort()
    out=0
    count=0
    for i in range(n-1):
        if(num[i]+1==num[i+1]):
            count+=1
            out=max(out,count)
        else:
            count=0
    print(out)