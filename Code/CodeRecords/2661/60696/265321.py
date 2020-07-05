def xor_res(n):
    num_of_one = 0
    num_of_zero = 0
    while n > 0:
        if n % 2 == 1:
            num_of_one += 1
        else:
            num_of_zero += 1
        n = n // 2
    return num_of_zero ^ num_of_one


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(xor_res(num))