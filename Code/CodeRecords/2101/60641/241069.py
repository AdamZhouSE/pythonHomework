def main():
    num = int(input())
    nums = []

    while True:
        nums.append(num)
        num = happy_num_convert(num)
        if num == 1:
            print(True)
            break
        elif num in nums:
            print(False)
            break


def happy_num_convert(num):
    nums = []
    result = 0

    while num > 0:
        nums.append(num % 10)
        num = num // 10

    for i in nums:
        result += i * i

    return result


if __name__ == "__main__":
    main()