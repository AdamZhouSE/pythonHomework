def combination(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(0, n-2):
            temp = b
            b = b+a
            a = temp
        return b


count = int(input())
ans = []
for i in range(0, count):
    num = int(input())
    ans.append(combination(num))
for j in ans:
    print(j)
