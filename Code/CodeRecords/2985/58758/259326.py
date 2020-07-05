def helper(n, now, s):
    if now > n:
        return s
    else:
        ch = chr(now+64)
        return helper(n, now+1, s+ch+s)


num = int(input())
print(helper(num, 1, ''))
