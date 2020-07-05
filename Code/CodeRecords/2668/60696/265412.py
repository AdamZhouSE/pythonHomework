def solve(n):
    digits = 0
    while n > 0:
        digits += 1
        n = n // 2
    new_num = pow(2, digits) - 1
    print('{:d} {:d}'.format(new_num-n, new_num))


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        solve(num)