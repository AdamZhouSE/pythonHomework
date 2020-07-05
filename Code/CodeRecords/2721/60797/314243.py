if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [a, b] = [int('0b' + a, 2) for a in input().split()]
        print(a*b)
