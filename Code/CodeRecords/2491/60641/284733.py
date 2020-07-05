def main():
    nums_1 = sorted(eval(input()))
    nums_2 = eval(input())
    result = []
    for num in nums_1:
        if num in nums_2 and result.count(num) < min(nums_1.count(num), nums_2.count(num)):
            result.append(num)
    print(result)


if __name__ == '__main__':
    main()
