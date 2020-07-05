input()
num = [int(x) for x in input().split()]
ans = set(num)
if len(ans) is 1:
    print(max(ans))
elif len(ans) is 2:
    print(max(ans) - min(ans))
elif len(ans) is 3:
    a = max(ans)
    b = min(ans)
    if (a + b) / 2 in ans:
        print(int((a + b) / 2) - b)
    else:
        print(-1)
else:
    print(-1)
