def main():
    time = int(input())
    result = []

    for i in range(0, time):
        length = int(input())
        nums = list(map(int, input().split(" ")))
        product = 1
        for j in range(0, length):
            product *= nums[j]
        for j in range(0, length):
            nums[j] = int(product / nums[j])
        result.append(" ".join(map(str, nums)) + " ")
    
    print("\n".join(result))


if __name__ == "__main__":
    main()
