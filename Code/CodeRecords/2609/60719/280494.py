def all_to_int(x):
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def handle_each_use_case():
    c = input().split(" ")
    c = all_to_int(c)
    l = [-1]*c[0]
    count = 0
    num = input().split(" ")
    i = c[0]-1
    t = 1
    for j in range(c[0]):
        if num[0] == num[j]:
            t += 1
    if t==c[0]:
        return -1
    while i>=0:
        if not (num[i] in l):
            l[count] = num[i]
            count += 1
            if count == c[1]:
                return num[i]
        i -= 1
    return -1


num = int(input())
for i in range(num):
    res = handle_each_use_case()
    print(res)