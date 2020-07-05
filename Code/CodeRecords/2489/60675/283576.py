import bisect
def func(nums:list,lower:int,upper:int) -> int:
    p = [0]
    for i in nums:
        p += [p[-1] + i]
    ans = 0
    q = []
    for pi in p[:]:
        i, j = pi + lower, pi + upper
        l = bisect.bisect_left(q, i)
        r = bisect.bisect_right(q, j)
        ans += r - l
        bisect.insort(q, pi)
    return ans



n = "l =" + input()
lower = int(input())
upper = int(input())
exec(n)
print(func(l,lower,upper))