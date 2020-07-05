nums = list(map(int, input().split(",")))
s = {-1: set()}
for n in sorted(nums):
    s[n] = max((s[d] for d in s if n % d == 0), key=len) | {n}
print(sorted(list(max(s.values(), key=len))))