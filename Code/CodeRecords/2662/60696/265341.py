def cal_one(n):
    num_of_one = 0
    while n > 0:
        if n % 2 == 1:
            num_of_one += 1
        n = n // 2
    if num_of_one % 2 == 0:
        return 'even'
    else:
        return 'odd'


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        num = int(input())
        print(cal_one(num))