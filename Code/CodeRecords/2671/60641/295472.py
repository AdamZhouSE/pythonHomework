def main():
    n = int(input())
    nums = []
    for i in range(0, n):
        nums.append(int(input()))
    dictionary = {
        0: 0,
        1: 0,
        2: 1
    }
    for i in range(0, len(nums)):
        print(consequent_one(nums[i], dictionary))


def consequent_one(num, dictionary):
    result = 0
    try:
        result += dictionary[num]
    except KeyError:
        for i in range(0, num - 1):
            if i == 0:
                result += (2 ** i - consequent_one(i, dictionary)) * (2 ** (num - 2 - i))
            else:
                result += (2 ** (i - 1) - consequent_one(i - 1, dictionary)) * (2 ** (num - 2 - i))
        dictionary[num] = result
    return result


if __name__ == '__main__':
    main()
