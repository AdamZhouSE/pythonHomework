if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, m] = [int(a) for a in input().split()]
        s = input().split()
        a = set(s)
        s = input().split()
        b = set(s)
        print(len(a | b))
