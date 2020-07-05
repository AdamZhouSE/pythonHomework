def max(num,nums):
    nums = list(map(int,nums.split(" ")))
    result = []
    for x in range(0,len(nums) - num + 1):
        temp = nums[x:x+num]
        temp.sort()
        result.append(temp[-1])
    return result

n = eval(input())
while(n != 0):
    n = n - 1
    num = int(input().split(" ")[1])
    print(" ".join(list(map(str,max(num,input())))))