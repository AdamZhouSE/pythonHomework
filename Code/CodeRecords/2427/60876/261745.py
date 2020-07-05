N=int(input())
for i in range(0,N):
    length=int(input())
    nums=list(map(int,input().split(" ")))
    jud=False
    for j in range(0,length):
        temp=nums[j]
        nums[j]=0
        if temp in nums:
            print(j+1)
            jud=True
            break
    if not jud:
        print(-1)