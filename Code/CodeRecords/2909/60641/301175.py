def main():
    string = input()
    max_letters = int(input())
    min_size = int(input())
    max_size = int(input())
    result = 0
    for i in range(min_size, max_size):
        for j in range(0, len(string) - i + 1):
            if different_letters(string[j:j + i]) == max_letters:
                result = max(result, string.count(string[j:j + i]))
    print(result)


def different_letters(s):
    dictionary = []
    for i in range(0, len(s)):
        if s[i] not in dictionary:
            dictionary.append(s[i])
    return len(dictionary)


if __name__ == '__main__':
    main()
