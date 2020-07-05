def point(x1, x2, y1, y2):
    return(abs(x1-x2) + abs(y1 - y2) == (((x1 - x2)**2 + (y1 - y2)**2)**.5))


if __name__ == "__main__":
    n = int(input())
    count = 0
    for i in range(n):
        m = int(input())
        X = []
        Y = []
        for j in range(m):
            x, y = input().split()
            X.append(int(x))
            Y.append(int(y))
        for j in range(m-1):
            for k in range(j+1, m):
                if point(X[j], X[k], Y[j], Y[k]):
                    count += 1
    print(count)