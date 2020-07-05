cnt=int(input())
for i in range(0,cnt):
    n=int(input())
    list1=list(map(int,input().split(' ')))
    res=0
    for j in range(1,len(list1)+1):
        for k in range(0,len(list1)+1-j):
            temp=1000000000000000000
            for t in range(k,k+j):
                temp=min(temp,list1[t])
            res=max(temp*j,res)
    print(res)