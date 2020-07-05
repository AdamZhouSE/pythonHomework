def search(string: str) -> list:
    res = []
    now = ''
    for i in string:
        if i.islower():
            now += i
        elif i == 'B':
            now = now[0:len(now)-1]
        elif i == 'P':
            res.append(now)
    return res


def find():
    s = input()
    ans = search(s)
    n = int(input())
    lst = []
    for j in range(n):
        c = input().split(' ')
        c = list(map(int, c))
        if c[0] < len(ans) + 1 and c[1] < len(ans) + 1:
            lst.append(str(ans[c[1]-1]).count(ans[c[0]-1]))
        else:
            lst.append(0)
    for j in lst:
        print(j)


find()