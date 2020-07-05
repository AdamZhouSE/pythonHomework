def main():
    nums = eval(input())
    length = int(input())
    standard = int(input())
    new_nums = []
    result = []

    for i in range(0, len(nums)):
        new_nums.append([abs(nums[i] - standard), nums[i] - standard,nums[i]])

    new_nums = sorted(new_nums,key=lambda x:x[0])

    for i in range(0, length):
        result.append(new_nums[i][2])
        
    result = sorted(result)
    print(result)

if __name__ == "__main__":
    main()