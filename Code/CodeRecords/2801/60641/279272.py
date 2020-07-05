def main():
    num = int(input())
    nums = sorted(list(map(int, input().split(" "))), reverse=True)
    result = False
    while len(nums) >= 3:
        if nums[0] < nums[1] + nums[2]:
            result = True
            break
        del nums[0]
    if result:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
