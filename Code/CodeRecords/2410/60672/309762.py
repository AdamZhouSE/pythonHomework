from collections import defaultdict

def longestSubsequence(arr, difference):
    size = len(arr)
    memo = defaultdict(lambda :size)
    cache = defaultdict(lambda :1)
    cache[arr[0]] = 1
    res = 1
    for i,j in enumerate(arr):
        memo[j] = min(memo[j], i)
    for i in range(1, size):
        k = int(arr[i]) - int(difference)
        if i > memo[k]:
            cache[arr[i]] = 1 + cache[k]
    # 最后返回最大值
    return  (max( res, max(list(cache.values()))))

arr=input()
difference=input()
ans=longestSubsequence(arr,difference)
print(ans)