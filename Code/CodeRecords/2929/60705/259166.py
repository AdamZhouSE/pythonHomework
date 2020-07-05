def solve():
    line1 = list(map(int, input().split(" ")))

    n = line1[0]
    m = line1[1]
    songs = []
    dis = []
    res = 0
    for i in range(0, n):
        songs.append(list(map(int, input().split(" "))))
        dis.append(songs[-1][0] - songs[-1][1])
        dis.sort()
        dis.reverse()
    a = 0
    b = 0
    ans = 0
    for i in range(0, n):
        a += songs[i][0]
        b += songs[i][1]
    if a <= m:
        return 0
    if b > m:
        return -1
    count = 0
    for i in range(0, n):
        count += 1
        a -= dis[i]
        if a < m:
            return count


if __name__ == '__main__':
    print(solve())
