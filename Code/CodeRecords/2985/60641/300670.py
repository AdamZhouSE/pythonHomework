def main():
    num = int(input())
    print(get_string(num))


def get_string(num):
    letters = ["\n", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
               "U", "V", "W", "X", "Y", "Z"]
    if num == 1:
        return letters[num]
    else:
        result = get_string(num - 1)
        result = result + letters[num] + result
        return result


if __name__ == '__main__':
    main()
