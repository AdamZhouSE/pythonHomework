def main():
    n = int(input())
    for i in range(0, n):
        num = int(input())
        num_of_zero = 0
        num_of_one = 0
        while num > 0:
            if num % 2 == 0:
                num_of_zero += 1
                num = num / 2
            else:
                num_of_one += 1
                num = (num - 1) / 2
        print(num_of_one ^ num_of_zero)


if __name__ == '__main__':
    main()
