def main():
    string = input()
    rank = []
    for i in range(0, len(string)):
        rank.append([i + 1, string[i:len(string)]])

    new_rank = sorted(rank, key=lambda x: x[1])
    result = []
    for i in range(0, len(new_rank)):
        result.append(new_rank[i][0])
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
