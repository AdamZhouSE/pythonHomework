def func2():
    t = int(input())
    while t>0:
        t -= 1
        temp = list(map(int, input().split(" ")))
        n = temp[0]
        k = temp[1]
        nums = list(map(int, input().split(" ")))
        res = 0
        for i in range(0,k):
            res += nums[i]
        for i in range(k+1,len(nums)+1):
            temp = 0
            for j in range(i-k,i):
                temp += nums[j]
            if temp > res:
                res = temp
        print(res)
    return
func2()