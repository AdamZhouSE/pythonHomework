n=int(input())
for x in range(0,n):
    length=int(input())
    numbers=list(map(int,input().split(" ")))
    res=[]
    for i in range(0,length):
        sum=1
        for j in range(0,length):
            if j!=i:
                sum=sum*numbers[j]
        res.append(sum)
    for i in range(0,length):
        if i==length-1:
            print(res[i],end=" ")
        else:
            print(res[i],end=" ")
    print("")