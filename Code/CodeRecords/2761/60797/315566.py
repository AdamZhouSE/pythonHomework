if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        res = 0
        for j in range(1,n+1):
            res += (n+1-j)**2
        print(res)

