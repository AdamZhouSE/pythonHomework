from typing import List
def maxLength(arr: List[str]) -> int:
    def helper(i, c):
        if i == len(arr): return bin(c).count('1')
        res = helper(i+1, c)
        for s in arr[i]:
            d = ord(s) - ord('a')
            if c & (1 << d):
                return res
        for s in arr[i]:
            d = ord(s) - ord('a')
            c |= 1 << d
        return max(res, helper(i+1, c))
    arr = [e for e in arr if len(set(e)) == len(e)]
    if len(arr) == 0: return 0
    return helper(0, 0)
a=input()
a=a[1:-1].split(',')
data = []
for i in a:
    data.append(i[1:-1])
print(maxLength(data))