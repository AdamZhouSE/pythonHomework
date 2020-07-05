def cal(string):
    temp = list(map(int,string.split(" ")))
    dict = {}
    for x in range(len(temp)):
        dict[temp[x] - 1] = x

    result = []
    for x in range(len(dict)):
        result.append(str(dict[x] + 1))
    return " ".join(result)

input()
print(cal(input()))