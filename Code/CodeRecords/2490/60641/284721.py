def main():
    nums = sorted(eval(input()))
    standard = eval(input())
    result = []
    for num in nums:
        if num in standard:
            result.append(num)
    print(result)


if __name__ == '__main__':
    main()
