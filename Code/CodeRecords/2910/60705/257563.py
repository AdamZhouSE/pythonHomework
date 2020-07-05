

def f(l):
    res = []
    res.append(max(l[0][0], l[0][1]))
    for i in range(1, len(l)):
        if min(l[i][0], l[i][1]) > res[i-1]:
            return "NO"
        elif max(l[i][0], l[i][1]) > res[i-1]:
            res.append(min(l[i][0], l[i][1]))
        else:
            res.append(max(l[i][0], l[i][1]))
    return "YES"


if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split(" "))))
    print(f(l))
