str=input()
target=int(input())
a=(len(str)-1)
str=str[1:a]
nums=list(map(int,str.split(",")))
for i in range(0,len(nums)):
    if nums[i]>target :
        print(-1)
        break;
    elif nums[i]==target :
        print(i)
        break;
