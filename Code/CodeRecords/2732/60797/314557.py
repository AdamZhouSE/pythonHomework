if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [a, b, c] = [int(a) for a in input().split()]
        print(pow(a, b) % c)
