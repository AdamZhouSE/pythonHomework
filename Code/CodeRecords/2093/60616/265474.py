def getPermutation(n: int, k: int) -> str:
    to_div = 1
    for i in range(2, n):
        to_div *= i
    nums = list(range(1, n + 1))
    res = ''
    n -= 1
    k -= 1
    while len(nums) > 1:
        i, k = divmod(k, to_div)
        res += str(nums.pop(i))
        to_div //= n  
        n -= 1
    return res + str(nums[0])


n=int(input())
k=int(input())
print(getPermutation(n,k))