num=int(input())
for i in range(num):
    temp=input().split(" ")
    length=int(temp[0])
    money=int(temp[1])
    
    nums=list(map(int,input().split(" ")))
    nums.sort()
    
    j=0
    sum=0
    while j<length and sum<=money:
        sum+=nums[j]
        j+=1
    if sum>money:
        j-=1
    print(j)