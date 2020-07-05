def main():
    rank = int(input())
    nums = []

    for i in range(0, rank+1):
        nums.append(str(i))

    s = "".join(nums)
    print(s[rank:rank+1])

if __name__ == "__main__":
    main()