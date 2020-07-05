left = int(input())
right = int(input())
result = []
for x in range(left,right+1):
    n = x
    judge = True
    while n > 0:
        tem = n % 10
        if tem == 0:
            judge = False
            break
        elif x % tem != 0:
            judge = False
            break
        else:
            n = n // 10
    if judge:
        result.append(x)
print(result)