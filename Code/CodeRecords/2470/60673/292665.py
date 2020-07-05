def test(n,nums):
    for j in range(n):
        for i in range(n):
            if(i==n-1 and j==n-1):
                print(nums[n-i-1][j],end=" ")
                print()
            else:
                print(nums[n-i-1][j],end="")
                print(" ",end="")

t=int(input())
for i in range(t):
    n=int(input())
    nums=input().split(" ")
    for i in range(len(nums)):
        nums[i]=int(nums[i])
    temp=[]
    j=0
    cal=0
    finnums = []
    while(j<len(nums)):
        cal=0
        while(cal<n):
            temp.append(nums[j])
            j+=1
            cal+=1
        finnums.append(temp)
        temp=[]


    test(n,finnums)




