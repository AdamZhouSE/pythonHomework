n = int(input())

ans = ''
while n > 0:
    t = ord('A') + (n-1) % 26
    ans = chr(t) + ans
    n = (n-1) // 26
print(ans)