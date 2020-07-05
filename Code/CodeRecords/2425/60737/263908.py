t = int(input())
while t:
    cmd = [int(n) for n in input().split( )]
    nums = [int(n) for n in input().split( )]
    l, k = cmd[0], cmd[1]
    ans = 0
    for i in nums:
        ans = i if abs(k-i)<=abs(k-ans) and i>ans else ans
    print(ans)
    t -= 1
    