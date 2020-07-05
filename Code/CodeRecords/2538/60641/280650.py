def main():
    nums = eval(input())
    for i in range(1, max(nums) + 2):
        if i not in nums:
            print(i)
            break


if __name__ == '__main__':
    main()
