if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, m] = [int(a) for a in input().split()]
        a = set(input().split())
        b = set(input().split())
        print(len(a | b))
