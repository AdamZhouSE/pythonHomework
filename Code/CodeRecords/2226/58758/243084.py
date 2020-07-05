def check(n):
    copy = n
    while copy != 0:
        num = copy % 10
        if num == 0:
            return False
        elif n % num != 0:
            return False
        else:
            copy //= 10
    return True


left = int(input())
right = int(input())
ans = []
for i in range(left, right+1):
    if check(i):
        ans.append(i)
print(ans)
