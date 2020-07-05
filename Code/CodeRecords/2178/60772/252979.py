def execute(arr,n):
    res = []
    s = "".join(arr)
    for i in range(n):
        for j in range(n-i):
            res.append(s[j:j+i+1])
    return len(set(res))


n = int(input())
nums = input().split()
arr = []
for i in range(n):
    arr.append(nums[i])
    print(execute(arr,len(arr)))
