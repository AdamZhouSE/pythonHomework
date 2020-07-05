import ast

def solve():
    data = ast.literal_eval(input())
    res = ''
    for i in range(0,len(data)):
        data[i] = str(data[i])
    data.sort(reverse=True)
    for i in range(0,len(data) -1):
        if len(data[i]) > len(data[i + 1]) and data[i + 1] in data[i] and data[i].index(data[i + 1]) == 0:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp
    for i in range(0,len(data)):
        res += data[i]
    print(res)

solve()