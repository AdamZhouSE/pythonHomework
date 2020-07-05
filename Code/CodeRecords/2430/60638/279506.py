n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    k=int(input())
    numbers.sort()
    res=[]
    for i in range(0,num-1):
        for j in range(i+1,num):
            if numbers[i]+numbers[j]==k:
                result=[i+1,j+1]
                res.append(result)
    if len(res)==0:
        print(-1)
    else:
        for i in range(0,len(res)):
            print(res[i][0],res[i][1],k)