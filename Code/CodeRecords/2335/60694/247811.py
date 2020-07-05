X = int(input())
Y = int(input())
cnt = 0
while X != Y:
    if X < Y:
        X = 2 * X
    else:
        X -= 1
    cnt += 1
print(cnt)
