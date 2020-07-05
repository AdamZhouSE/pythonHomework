def maxTrainingDays(nums):
    nums.sort()
    res = len(nums)
    i = 0
    d= 1
    while(i<len(nums)):
        #print(" i before:",i)
        #print(" d before:",d)
        if(nums[i]<d):
            i+=1
        else:
            i+=1
            d+=1
        #print(" i after",i)
        #print(" d after",d)
    #if(d==3):
        #print(nums)

    return d-1
numOfGames = int(input())
temp = input().split(" ")
nums = []
for t in temp:
    nums.append(int(t))
print(maxTrainingDays(nums))