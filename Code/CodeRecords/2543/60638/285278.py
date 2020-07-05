n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    for i in range(1,len(numbers)+1):
        res=[]
        for j in range(0,len(numbers)-i+1):
            res.append(min(numbers[j:j+i]))
        if i !=len(numbers):
            print(max(res),end=" ")
        else:
            print(max(res))
           