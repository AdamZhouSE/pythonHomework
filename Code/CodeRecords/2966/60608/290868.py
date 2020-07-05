

def func16():
    for _ in range(0, eval(input())):
        arr = list(map(int, input().split()))
        n: int = arr[0]
        s = "".join(input().split())
        t = "".join(input().split())
        res, start = [], 0
        for i in range(0, 3):
            for j in range(n, start, -1):
                k = t.find(s[start:j])
                if k >= 0:
                    res.append((k + 1, k + (j - start), start))
                    start = j
                    break
        res = sorted(res, key=lambda x: x[0])
        flag = True
        for i in range(0, len(res)):
            k = res[i]
            if i == 0:
                if k[0] != 1:
                    flag = False
                    break
            if i == len(res) - 1:
                if k[1] != n:
                    flag = False
                    break
            if i != 0:
                if k[0] - res[i - 1][1] != 1:
                    flag = False
                    break
        if flag and len(res) <= 3:
            print('YES')
            res = sorted(res, key=lambda x: x[2])
            if len(res) == 1:
                print('1 %d' % (n - 2))
                print('%d %d' % (n - 1, n - 1))
                print('%d %d' % (n, n))
            if len(res) == 2:
                if res[1][1] - res[1][0] > 0:
                    print('%d %d' % (res[0][0], res[0][1]))
                    print('%d %d' % (res[1][0], res[1][0]))
                    print('%d %d' % (res[1][0] + 1, res[1][1]))
                else:
                    print('%d %d' % (res[0][0], res[0][1] - 1))
                    print('%d %d' % (res[0][1], res[0][1]))
                    print('%d %d' % (res[1][0], res[1][1]))
            else:
                for item in res:
                    print(item[0], end=' ')
                    print(item[1])
        else:
            print('NO')


func16()
