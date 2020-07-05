n = 0
num = []
flag = False


def search(s, x):
    global flag
    if s % 360 == 0:
        if x == n:
            flag = True
    if x > n - 1:
        return
    if flag:
        return
    search(s - num[x], x + 1)
    search(s + num[x], x + 1)


if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        num.append(int(input()))
    num.sort()

    search(2880, 0)
    if flag:
        print("YES")
    else:
        print("NO")