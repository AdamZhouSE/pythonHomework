def main():
    nums = eval(input())
    while nums[0] == min(nums):
        del nums[0]
    while nums[len(nums) - 1] == max(nums):
        del nums[len(nums) - 1]
    print(len(nums))


if __name__ == "__main__":
    main()
