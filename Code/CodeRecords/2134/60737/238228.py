import math


def dead_pig(buckets, die_time, test_time):
    time = test_time / die_time + 1
    num = 0
    while math.pow(time, num) < buckets:
        num += 1
    return num


if __name__ == "__main__":
    buckets = int(input())
    die_time = int(input())
    test_time = int(input())
    print(dead_pig(buckets, die_time, test_time))
