def main():
    string1 = input().strip()
    string2 = input().strip()
    count = 0

    for i in range(1, len(string1) + 1):
        for j in range(0, len(string1) - i + 1):
            for k in range(0, len(string2) - i + 1):
                if j == k:
                    continue
                else:
                    if string1[j:j + i] == string2[k:k + i]:
                        count += 1

    print(count, end="")


if __name__ == "__main__":
    main()
