sum=int(input())
for i in range(0,sum):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    result=[]
    for j in range(0,length):
        sum=1
        for index in range(0,length):
            if index==j:
                continue
            else:
                sum*=nums[index]
        print(sum,end=" ")
    print()