def bit(num: int) -> list:
    res = []
    index = num
    while index >= 0:
        if index & num == index:
            res.append(index)
        index -= 1
    return res


t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    ans.append(bit(n))
for i in ans:
    for j in range(len(i)-1):
        print(str(i[j]) + ' ', end='')
    print(str(i[len(i)-1]) + ' ')
