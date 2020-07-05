if __name__ == '__main__':
    n = int(input())
    f, d, c, ind = [0 for _ in range(n+1)], [0 for _ in range(n+1)], [0 for _ in range(n+1)], [0 for _ in range(n+1)]
    now = [0 for _ in range(n+1)]
    ans = 0
    for i in range(1, n+1):
        temp1 = input().split(' ')[0:3]
        temp1 = list(map(int, temp1))
        f[i], d[i], c[i] = temp1[0], temp1[1], temp1[2]
        if f[i] != -1:
            ind[f[i]] += 1
    queue = []
    for i in range(1, n+1):
        if ind[i] == 0:
            queue.append(i)
    while len(queue) != 0:
        t = queue[0]
        if d[t] > now[t]:
            ans += c[t] * (d[t] - now[t])
        if t != 1:
            c[f[t]] = min(c[f[t]], c[t])
            now[f[t]] += max(d[t], now[t])
            ind[f[t]] -= 1
            if ind[f[t]] == 0:
                queue.append(f[t])
        queue.pop(0)
    print(ans)