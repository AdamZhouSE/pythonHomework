def main():
    nums = eval(input())
    result = []
    for i in range(0, len(nums)):
        if len(result) == 0:
            result.append(nums[i])
        else:
            result += [max(nums) + 1]
            for j in range(0, len(result)):
                if nums[i] < result[j]:
                    result.insert(j, nums[i])
                    break
            result = result[:len(result) - 1]
    print(result)


if __name__ == '__main__':
    main()