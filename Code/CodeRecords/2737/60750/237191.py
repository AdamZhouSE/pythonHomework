import ast


def solve(data):
    a = 0
    b = 0
    num_a = 0
    num_b = 0
    for i in range(0,len(data)):
        if data[i] == a:
            num_a = num_a + 1
        elif data[i] == b:
            num_b = num_b + 1
        elif num_a == 0:
            a = data[i]
        elif num_b == 0:
            b = data[i]
        else:
            num_a = num_a - 1
            num_b = num_b - 1
    num_b = 0
    num_a = 0
    for i in range(0,len(data)):
        if data[i] == a:
            num_a = num_a + 1
        if data[i] == b:
            num_b = num_b + 1
    res = []
    if num_a > (len(data) // 3):
        res.append(a)
    if num_b > (len(data) // 3):
        res.append(b)
    return res


data = ast.literal_eval(input())
print(solve(data))
