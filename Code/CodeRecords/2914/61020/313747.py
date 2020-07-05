def read_a_num_list():
    result = input().split()
    return [int(x) for x in result]


def is_all_same(a_list):
    if len(a_list) == 1:
        return True

    return a_list[0] == a_list[1] and is_all_same(a_list[1:])


def is_possible_diff(diff):
    if is_all_same(diff) and diff[0] == 0:
        return True

    # i = 0
    # while True:
    #     if diff[i] != 0:
    #         break
    #     i += 1
    # j=0
    # while True:
    #     if diff[j]!=0:
    #         pass

    for i, v in enumerate(diff):
        if v != 0:
            for i_, v_ in enumerate(reversed(diff)):
                if v_ != 0:
                    return is_all_same(diff[i:n - i_]) and diff[i] < 0


t = int(input())
for i in range(t):
    n = int(input())
    a = read_a_num_list()
    b = read_a_num_list()
    difference = [x - y for x, y in zip(a, b)]

    if is_possible_diff(difference):
        print("YES")
    else:
        print("NO")
