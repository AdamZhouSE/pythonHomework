def main():
    string = list(input())
    element = sorted(list(set(string)))
    rank = []
    result = []

    for i in string:
        rank.append(element.index(i) + 1)

    offset = 1
    while len(rank) != len(list(set(rank))):
        for i in range(0, len(string)):
            try:
                rank[i] = rank[i] * 10 + element.index(string[i + offset]) + 1
            except:
                rank[i] = rank[i] * 10
        new_element = sorted(list(set(rank)))
        new_rank = []
        for i in rank:
            new_rank.append(new_element.index(i) + 1)
        rank = new_rank
        offset += 1

    result_list = list(zip(string, rank, range(1, len(string) + 1)))
    result_list = sorted(result_list, key=lambda x: x[1])
    for i in result_list:
        result.append(i[2])

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
