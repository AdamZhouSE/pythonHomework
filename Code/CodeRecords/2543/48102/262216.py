def windows(ls: list) -> list:
    res = []
    for i in range(1, len(ls)+1):
        temp = []
        for j in range(len(ls)-i+1):
            min_v = min(ls[j:j+i])
            temp.append(min_v)
        res.append(max(temp))
    return res


t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    lst = input().split(' ')
    lst = list(map(int, lst))
    ans.append(windows(lst))
for k in ans:
    for m in range(len(k)-1):
        print(str(k[m]) + ' ', end='')
    print(k[len(k)-1])