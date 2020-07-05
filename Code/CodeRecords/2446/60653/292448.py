if __name__ == '__main__':
    nex = [[0]*26 for i in range(0, 1000)]
    cnt = 0
    b = [[False]*110 for i in range(0, 1000)]
    n = int(input())
    for i in range(1, n+1):
        s = input().split(' ')
        x = int(s[0])
        for j in range(1, x+1):
            t = list(s[j])
            now = 0
            for a in t:
                p = ord(a) - ord('a')
                if nex[now][p] == 0:
                    cnt += 1
                    nex[now][p] = cnt
                now = nex[now][p]
            b[now][i] = True
    m = int(input())
    for i in range(0, m):
        s = list(input())
        bb = True
        now = 0
        flag = True
        for a in s:
            p = ord(a) - ord('a')
            if nex[now][p] == 0:
                flag = False
                break
            now = nex[now][p]
        if flag:
            for j in range(1, n+1):
                if b[now][j]:
                    bb = False
                    print(j, end=' ')
        if bb:
            print('', end=' ')
        print()