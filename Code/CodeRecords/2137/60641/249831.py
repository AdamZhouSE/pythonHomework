def main():
    num = int(input())
    sum = 0

    for i in range(1,num):
        if num % i == 0:
            sum += i

    if num == sum:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()