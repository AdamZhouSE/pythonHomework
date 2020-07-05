def peidui(n: int, ls: list, k: int):
    res = []
    for i in range(n-1):
        if ls[i] < k - ls[i]:
            if k - ls[i] in ls:
                res.append([ls[i], k - ls[i], k])
        else:
            break
    if len(res) == 0:
        return -1
    else:
        return res


t = int(input())
ans = []
for j in range(t):
    num = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    k_sum = int(input())
    ans.append(peidui(num, lst, k_sum))
for j in ans:
    if type(j) == int:
        print(j)
    else:
        for m in j:
            for n in range(len(m)-1):
                print(str(m[n]) + ' ', end='')
            print(m[len(m)-1])