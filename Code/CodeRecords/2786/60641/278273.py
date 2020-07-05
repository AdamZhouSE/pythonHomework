def main():
    num = int(input())
    nums = list(map(int, input().split(" ")))
    nums = list(reversed(sorted(nums)))
    is_stopped = False
    for i in range(0, num):
        if nums[i] < i + 1:
            print(i + 1)
            is_stopped = True
            break
    if not is_stopped:
        print(num)


if __name__ == "__main__":
    main()
