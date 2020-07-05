left = int(input())
right = int(input())
res = []
for num in range(left, right + 1):
    ls = str(num)
    ls = list(map(int, ls))
    flag = True
    for n in ls:
        if (n == 0) or (num % n != 0):
            flag = False
            break
    if flag:
        res.append(num)
print(res)