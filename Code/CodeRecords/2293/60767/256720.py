def selectKthNumber(nums,k):
    temp = nums[0:k]
    temp.sort()
    for i in range(k,len(nums)):
        if(nums[i]<temp[-1]):
            temp[-1]=nums[i]
            temp.sort()
    return temp[-1]

numOfTests = int(input())
temp = []
for i in range(numOfTests):
    n = int(input())
    nums = []
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    k = int(input())
    print(selectKthNumber(nums,k))
