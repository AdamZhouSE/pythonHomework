maxn = 100005
y, nex, las, cnt, tot = [0]*(2*maxn), [0]*(2*maxn), [0]*maxn, [0]*maxn, 0
f, ans = [0]*maxn, True
N, K = 0, 0


def dfs(x):
    global f, cnt, las, nex, y, K, ans
    f[x] = 1
    cnt[x] = 1
    j = las[x]
    while j:
        if not f[y[j]]:
            dfs(y[j])
            if not ans:
                return
            if cnt[y[j]] < K:
                cnt[x] += cnt[y[j]]
                if cnt[x] > K:
                    ans = False
                    return
            elif cnt[y[j]] > K:
                ans = False
                return
        j = nex[j]


if __name__ == "__main__":
    T = int(input())
    while T:
        y, nex, las, cnt, tot = [0] * (2 * maxn), [0] * (2 * maxn), [0] * maxn, [0] * maxn, 0
        f = [0] * maxn
        c1 = [int(i) for i in input().split( )]
        N, K = c1[0], c1[1]
        for i in range(N-1):
            cmd = [int(i) for i in input().split( )]
            a, b = cmd[0], cmd[1]
            tot += 1
            y[tot] = b
            nex[tot] = las[a]
            las[a] = tot
            tot += 1
            y[tot] = a
            nex[tot] = las[b]
            las[b] = tot
        ans = True
        dfs(1)
        print("YES" if ans else "NO")
        T -= 1
