if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [m,n, a, b] = [int(a) for a in input().split()]
        res = 0
        for j in range(m,n+1):
            if j%a==0 or j%b==0:
                res += 1
        print(res)
