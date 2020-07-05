def main():
    nums = list(map(int,input().split(",")))
    sums = []

    for i in range(0,len(nums)):
        sum = 0

        for j in range(0,len(nums)):
            sum += j * nums[(j+i)%len(nums)]

        sums.append(sum)

    print(max(sums))

if __name__ == "__main__":
    main()