def dfs(x: int, d: int):
    global ans
    global t
    global flag
    if d >= ans:
        return
    if x > t:
        ans = d
        return
    flag[x] = 0
    while flag[x] < 2:
        cnt[0] = 0
        cnt[1] = 0
        for i in range(1, x):
            if r[i] > l[x]:
                if flag[i] == flag[x] and r[i] < r[x]:
                    cnt[1] += 1
                else:
                    cnt[0] += 1
        flag[x] += 1
    dfs(x+1, d+min(cnt[0], cnt[1]))


def work():
    global l
    global r
    global t
    global ans
    global a
    global n
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.insert(0, 0)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if a[i] == a[j]:
                t += 1
                l[t] = i
                r[t] = j
    ans = 10 ** 5
    dfs(1, 0)
    print(ans)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = 0
        ans = 0
        t = 0
        a = []
        l = [0] * 50
        r = [0] * 50
        flag = [0] * 50
        cnt = [0, 0]
        work()
