def main():
    time = int(input())

    for i in range(0, time):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        product = 1
        for j in range(0, length):
            product *= nums[i]
        for j in range(0, length):
            nums[i] = product / nums[i]
        print(" ".join(map(str, nums)))


if __name__ == "__main__":
    main()
