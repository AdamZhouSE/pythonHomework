def main():
    nums = eval(input())
    even_nums = []
    i = 0
    while i < len(nums):
        try:
            while nums[i] % 2 == 0:
                even_nums.append(nums[i])
                del nums[i]
            i += 1
        except IndexError:
            break
    print(even_nums + nums)


if __name__ == "__main__":
    main()
