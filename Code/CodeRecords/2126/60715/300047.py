def largest(nums) :
    s = {-1: set()}
    for n in sorted(nums):
        s[n] = max((s[d] for d in s if n % d == 0), key=len) | {n}
    return list(max(s.values(), key=len))
nums=list(map(int,input().split(',')))
print(largest(nums))