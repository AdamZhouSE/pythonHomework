def main():
    nums = eval(input())
    length_of_maximum = len(str(max(nums)))
    for i in range(0, len(nums)):
        nums[i] = [nums[i],
                   str(nums[i]) + str(nums[i])[len(str(nums[i])) - 1] * (length_of_maximum - len(str(nums[i])))]
    nums = sorted(nums, key=lambda x: x[1],reverse=True)
    result = ""
    for i in range(0, len(nums)):
        result += str(nums[i][0])
    print(result)


if __name__ == "__main__":
    main()
