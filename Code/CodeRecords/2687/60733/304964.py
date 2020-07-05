def num_having_alternate_bit(n):
    initial = 1
    while n > initial:
        print(initial, end=' ')
        if initial % 2 == 1:
            initial *= 2
        else:
            initial *= 2
            initial += 1
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        num_having_alternate_bit(n)