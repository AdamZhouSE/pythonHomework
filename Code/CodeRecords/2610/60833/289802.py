n=int(input())
for i in range(0,n):
    length=int(input())
    numlist=list(map(int,input().split(' ')))
    res=0
    for j in range(1,length+1):
        for k in range(0,length-j+1):
            temp=numlist[k:k+j]
            if len(set(temp))==len(temp):
                res+=len(temp)
    print(res)