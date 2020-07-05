def findMassNum(nums):
    times=len(nums)//3
    dict={}
    for i in nums:
        dict[i] = dict.get(i,0)+1
    ans = []
    for key in dict.keys():
        if dict[key]>times:  ans.append(key)
    return ans

lst=eval(input())
print(findMassNum(lst))