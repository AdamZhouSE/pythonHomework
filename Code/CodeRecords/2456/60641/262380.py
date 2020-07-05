def main():
    nums = eval(input())
    result = []
    for i in range(0, len(nums)):
        result.append(sorted(nums[i:]).index(nums[i]))
    print(result)


if __name__ == "__main__":
    main()
