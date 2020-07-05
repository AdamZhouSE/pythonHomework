def unglyNum(a, b, c, n):
    ctr = 0
    p = min(a, b, c)
    res = [0]
    p1 = 0
    p2 = 0
    p3 = 0
    res.append(p)
    for i in range(n):
        res.append(min(res[p1] + a, res[p2] + b, res[p3] + c))
        if res[-1] % a == 0:
            p1 = len(res) - 1
        if res[-1] % b == 0:
            p2 = len(res) - 1
        if res[-1] % c == 0:
            p3 = len(res) - 1
   
    return res[-1]

if __name__ == '__main__':
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    p = unglyNum(a, b, c, n)
    print(p);

