def main():
    string1 = input().strip()
    string2 = input().strip()
    count = 0
    dictionary1 = []
    count_dictionary1 = []
    dictionary2 = []
    count_dictionary2 = []

    for i in range(1, len(string1) + 1):
        for j in range(0, len(string1) - i + 1):
            if string1[j:j + i] not in dictionary1:
                dictionary1.append(string1[j:j + i])
                count_dictionary1.append(1)
            else:
                count_dictionary1[dictionary1.index(string1[j:j + i])] += 1

    for i in range(1, len(string2) + 1):
        for j in range(0, len(string2) - i + 1):
            if string2[j:j + i] not in dictionary2:
                dictionary2.append(string2[j:j + i])
                count_dictionary2.append(1)
            else:
                count_dictionary2[dictionary2.index(string2[j:j + i])] += 1

    for i in range(0, len(dictionary1)):
        while True:
            try:
                if dictionary1[i] not in dictionary2:
                    del dictionary1[i]
                    del count_dictionary1[i]
                else:
                    break
            except:
                break

    for i in range(0, len(dictionary2)):
        while True:
            try:
                if dictionary2[i] not in dictionary1:
                    del dictionary2[i]
                    del count_dictionary2[i]
                else:
                    break
            except:
                break

    dict1 = list(zip(dictionary1, count_dictionary1))
    dict2 = list(zip(dictionary2, count_dictionary2))
    dict1 = sorted(dict1, key=lambda x: x[0])
    dict2 = sorted(dict2, key=lambda x: x[0])

    for i in range(0, len(dict1)):
        count += dict1[i][1] * dict2[i][1]

    print(count, end="")


if __name__ == "__main__":
    main()
