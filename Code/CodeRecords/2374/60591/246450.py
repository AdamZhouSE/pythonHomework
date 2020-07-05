dic = {}
def sortByValue(num):
    return dic[num]

def sortBy(nums):
    nums = list(map(int,nums.split(" ")))
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    keys = list(dic.keys())
    keys.sort(key = sortByValue)
    result = []
    for key in keys:
        while(dic[key]!=0):
            dic[key] -= 1
            result.append(key)
    result = list(map(str,result))
    result.reverse()
    print(" ".join(result) +" ")

n = eval(input())
while(n != 0):
    n = n - 1
    input()
    sortBy(input())
