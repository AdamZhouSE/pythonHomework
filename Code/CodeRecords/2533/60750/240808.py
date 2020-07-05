import ast


def solve():
    data = ast.literal_eval(input())
    for i in range(0,len(data)):
        if data[i] % 2 == 0:
            temp = data[i]
            del data[i]
            data = [temp] + data
    print(data)
    return


solve()