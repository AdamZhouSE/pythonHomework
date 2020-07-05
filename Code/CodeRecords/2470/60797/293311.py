
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        line = [int(a) for a in input().split()]
        ptr = 0
        data = [[0 for i in range(n)]for i in range(n)]
        for j in range(n-1,-1,-1):
            for i in range(n):
                data[i][j] = line[ptr]
                ptr += 1
        for i in range(n):
            for j in range(n):
                print(data[i][j], end=' ')
        print()

