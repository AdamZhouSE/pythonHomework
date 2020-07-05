def func47():
    n = int(input())
    nums = list(map(int, input().split(" ")))
    a = 0
    neg = []
    pos = []
    for i in nums:
        if i < 0:
            a += 1
            neg.append(i)
        if i > 0:
            pos.append(i)
    b = nums.count(0)
    ans = -1*a - sum(neg) + b + sum(pos) - len(pos)
    if b==0 and a%2==1:
        ans += 2
    print(ans)
    return
func47()