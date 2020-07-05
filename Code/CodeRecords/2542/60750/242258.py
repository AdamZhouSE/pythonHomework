import ast


def longest():
    count = []
    data = ast.literal_eval(input())
    data.sort()
    tmp = 1
    for i in range(0,len(data) - 1):
        if data[i + 1] - data[i] == 1:
            tmp += 1
        else:
            if tmp != 1:
                count.append(tmp)
                tmp = 1
    if tmp != 1:
        count.append(tmp)
    count.sort()
    if len(count) == 0:
        print(0)
        return
    print(count[len(count) - 1])
    return


longest()