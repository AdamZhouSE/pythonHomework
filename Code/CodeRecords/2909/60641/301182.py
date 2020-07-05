def main():
    string = input()
    max_letters = int(input())
    min_size = int(input())
    max_size = int(input())
    result = 0
    sub_string = []
    for i in range(min_size, max_size + 1):
        sub_strings = []
        for j in range(0, len(string) - i + 1):
            sub_strings.append(string[j:j + i])
        sub_string.append(sub_strings)

    for i in range(0, len(sub_string)):
        for j in range(0, len(sub_string[i])):
            if different_letters(sub_string[i][j]) == max_letters:
                result = max(result, sub_string[i].count(sub_string[i][j]))
    print(result)


def different_letters(s):
    dictionary = []
    for i in range(0, len(s)):
        if s[i] not in dictionary:
            dictionary.append(s[i])
    return len(dictionary)


if __name__ == '__main__':
    main()
