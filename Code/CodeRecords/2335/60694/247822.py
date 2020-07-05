X = int(input())
Y = int(input())
cnt = 0
while X != Y:
    if X < Y:
        if (X-1) * 2 == Y:
            cnt += 2
            break
        X = 2 * X
    else:
        X -= 1
    cnt += 1
print(cnt)
