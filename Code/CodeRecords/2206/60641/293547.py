from functools import reduce


def main():
    n = int(input())
    nums = {
        1: 1
    }
    for i in range(0, n):
        num = int(input())
        print(find_num(num, nums))


def find_num(num, dictionary):
    try:
        result = dictionary[num]
    except KeyError:
        result = find_num(num - 1, dictionary)
        temp = list(range(int((num * (num + 1)) / 2) - num + 1, int((num * (num + 1)) / 2) + 1))
        result += reduce(lambda x, y: x * y, temp)
        dictionary[num] = result
    return result


if __name__ == '__main__':
    main()
