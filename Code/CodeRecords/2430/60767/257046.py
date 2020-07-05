def ans(nums,k):
    res = []
    flag = 0
    for i in range(len(nums)):
        for j in range(0,i):
            if(nums[i]!=nums[j] and nums[i]+nums[j]==k):
                temp = [min(nums[i],nums[j]),max(nums[i],nums[j])]
                if temp not in res:
                    res.append(temp)
                    flag = 1
    if(flag==0):
        return -1
    else:
        res.sort()
        return res

numOfTests = int(input())
temp = []
for i in range(numOfTests):
    n = int(input())
    nums = []
    temp = input().split(" ")
    for t in temp:
        nums.append(int(t))
    k = int(input())
    res = ans(nums,k)
    if(res==-1):
        print(res)
    else:
        for i in range(len(res)):
            for x in res[i]:
                print(x,"",end="")
            print(k)


