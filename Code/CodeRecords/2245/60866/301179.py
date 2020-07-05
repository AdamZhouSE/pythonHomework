def binaryGap(N):
    last = None
    ans = 0
    for i in range(32):
        if (N >> i) & 1:
            if last is not None:
                ans = max(ans, i - last)
            last = i
    return ans
a=int(input())
print(binaryGap(a))