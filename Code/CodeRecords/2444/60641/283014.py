def main():
    information = input().split("]")
    nums = eval("[" + information[0].split("[")[1] + "]")
    k = int(information[1][6])
    t = int(information[1][13])
    existence = False
    for i in range(1, min(len(nums), k + 1)):
        for j in range(0, len(nums) - i):
            if abs(nums[j] - nums[j + i]) <= t:
                existence = True
                break
        if existence:
            break
    if existence:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()
