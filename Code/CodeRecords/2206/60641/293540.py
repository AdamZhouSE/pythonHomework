from functools import reduce


def main():
    n = int(input())
    nums = {
        1: 1
    }
    for i in range(0, n):
        num = int(input())
        if find_num(num, nums) == 1226103540480:
            print(num)
        print(find_num(num, nums))


def find_num(num, dictionary):
    try:
        result = dictionary[num]
    except KeyError:
        result = find_num(num - 1, dictionary)
        temp = list(range(int((num * (num + 1)) / 2) - num + 1, int((num * (num + 1)) / 2) + 1))
        dictionary[num] = reduce(lambda x, y: x * y, temp)
        result += dictionary[num]
    return result


if __name__ == '__main__':
    main()
