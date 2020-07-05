def transform(n):
    temp = pow(2, 32) - 1
    i = 0
    while i < 31:
        if n & (0x1<<i) and n & (0x1<<(i+1)):
            i += 2
        elif n & (0x1<<i) == 0 and n & (0x1<<(i+1)) == 0:
            i += 2
        elif n & (0x1<<i):
            n = n & (temp - (0x1<<i))
            n = n | (0x1<<(i+1))
            i += 2
        else:
            n = n | (0x1<<i)
            n = n & (temp - (0x1<<(i+1)))
            i += 2
    return n


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(transform(num))