if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        line = list(map(int, input().split(" ")))
        if n > 5:
            print(1)
        else:
            print(0)
        