if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, money] = [int(a) for a in input().split()]
        res = money * (n+1)/2
        print(res)
