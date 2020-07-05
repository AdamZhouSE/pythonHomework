def main():
    nums = list(map(int, input().split(" ")))
    num_of_queen = nums[0]
    num_of_interest = nums[1]
    queens = [""]
    result = []
    for i in range(0, num_of_queen):
        information = input().split(" ")
        queens.append(information[0] + queens[int(information[1])])
    for i in range(0, num_of_interest):
        tag = input()
        result.append([tag, 0])
        for j in range(1, num_of_queen + 1):
            if queens[j].startswith(tag):
                result[i][1] += 1

    for i in range(0, num_of_interest):
        print(result[i][1])


if __name__ == "__main__":
    main()
