def getNum(n):
    if n % 2 != 0:
        k = int(n / 2 + 1)
        return int(pow(2, pow(2, k - 1)))
    else:
        k = int(n / 2)
        return int(pow(2, pow(3, k - 1)))

n = int(input())

t_list = []
ans_list = []
for i in range(n):
    t = int(input())
    ans = getNum(t)
    t_list.append(t)
    ans_list.append(ans)
    print(ans)