import ast

def solve(data):
    i = 0
    while(i < len(data) - 1):
        if data[i] != data[i + 1]:
            return data[i]
        else:
            i = i + 2
    return 0
data = ast.literal_eval(input())
print(solve(data))