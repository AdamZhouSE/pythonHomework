def main():
    nums = list(map(int, input().split(",")))
    print(sum(range(1, max(nums) + 1)) - sum(nums))


if __name__ == "__main__":
    main()