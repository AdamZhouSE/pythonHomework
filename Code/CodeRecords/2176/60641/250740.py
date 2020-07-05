def main():
    string = list(input())
    new_string = sorted(set(string))
    result = []

    for i in new_string:
        result = result + find_index(string, i, 0)

    print(" ".join(map(str, result)))


def find_index(string, s, start):
    result = []
    num = string.index(s, start) + 1
    try:
        result = find_index(string, s, num) + result
    except ValueError:
        pass
    result.append(num)
    return result


if __name__ == "__main__":
    main()
