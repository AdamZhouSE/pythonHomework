def main():
    nums = sorted(eval(input()), reverse=True)
    result = 0
    for i in range(0, len(nums)):
        if nums[i] >= i + 1:
            result = i + 1
            break
    print(result)


if __name__ == '__main__':
    main()
