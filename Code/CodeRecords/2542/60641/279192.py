def main():
    nums = eval(input())
    result = [min(nums)]
    nums.remove(result[0])
    while True:
        minimum = min(nums)
        if minimum - result[len(result) - 1] == 1:
            result.append(minimum)
            nums.remove(minimum)
        else:
            break
    print(len(result))


if __name__ == "__main__":
    main()
