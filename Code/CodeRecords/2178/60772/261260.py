#求字符串的所有字串

def cut(s):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            results.append(s[i:i + x + 1])
    return results

def execute(arr):
    arr = cut("".join(arr))
    return len(set(arr))


n = int(input())
nums = input().split()
arr = []
for i in range(n):
    arr.append(nums[i])
    print(execute(arr))


