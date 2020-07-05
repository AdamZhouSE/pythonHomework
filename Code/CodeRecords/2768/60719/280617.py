def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def handle_each_use_case():
    tar = input().split(" ")
    tar = all_to_int(tar)
    res = 0
    for i in range(tar[0], tar[1]+1):
        if i % tar[2] == 0:
            res += 1
    return res


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)