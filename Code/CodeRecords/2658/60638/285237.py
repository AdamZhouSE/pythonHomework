n=int(input())
for x in range(0,n):
    nums=list(map(int,input().split(" ")))
    numbers=list(map(int,input().split(" ")))
    num=nums[0]
    k=nums[1]
    res=0
    for i in range(0,num):
        if numbers[i]%k==0:
            res=res|numbers[i]
    print(res)