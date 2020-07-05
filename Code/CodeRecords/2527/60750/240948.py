import ast


def restaurant():
    data = ast.literal_eval(input())
    v_friendly = int(input())
    max_price = int(input())
    max_distance = int(input())
    if v_friendly == 1:
        i = 0
        while i < len(data):
            if data[i][2] == 0:
                del data[i]
            else:
                i = i + 1
    j = 0
    while j < len(data):
        if data[j][3] > max_price or data[j][4] > max_distance:
            del data[j]
        else:
            j = j + 1
    res = []
    data.sort(key=lambda k:k[1],reverse=True)
    m = 0
    tmp = []
    count = 0
    while m < len(data) - 1:
        if data[m][1] > data[m + 1][1]:
            if data[m][1] != count:
                tmp.sort(reverse=True)
                res += tmp
                res.append(data[m][0])
                tmp = []
            else:
                tmp.append(data[m][0])
        else:
            tmp.append(data[m][0])
            count = data[m][1]
        m += 1
        if m == len(data) - 1:
            if data[m][1] == data[m - 1][1]:
                tmp.append(data[m][0])
                tmp.sort(reverse=True)
                res += tmp
            else:
                res += [data[m][0]]
    print(res)
    return

restaurant()


