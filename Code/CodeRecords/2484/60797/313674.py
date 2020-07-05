if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, m] = [int(a) for a in input().split()]
        s = input()
        a = set(s)
        s = input()
        b = set(input())
        print(len(a | b))
