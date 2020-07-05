import math


def main():
    num_of_groups = int(input())
    num_of_each_group = list(map(int, input().split(" ")))
    count = [0, num_of_each_group.count(1), num_of_each_group.count(2), num_of_each_group.count(3),
             num_of_each_group.count(4)]
    result = 0

    result += count[4]
    count[4] = 0

    if count[1] <= count[3]:
        result += count[3]
        count[1] = 0
        count[3] = 0
        result += math.ceil(count[2] / 2)
        count[2] = 0
    else:
        result += count[3]
        count[1] -= count[3]
        count[3] = 0
        if count[2] % 2 == 0:
            result += count[2] / 2
            result += math.ceil(count[1] / 4)
            count[2] = 0
            count[1] = 0
        else:
            result += math.floor(count[2] / 2)
            if count[1] <= 2:
                result += 1
                count[2] = 0
                count[1] = 0
            else:
                result += 1
                count[2] = 0
                count[1] -= 2
                result += math.ceil(count[1] / 4)

    result = int(result)
    print(result)


if __name__ == "__main__":
    main()
