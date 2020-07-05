import ast

def solve():
    data = ast.literal_eval(input())
    res = ''
    for i in range(0,len(data)):
        data[i] = str(data[i])
    data.sort(reverse=True)
    for i in range(0,len(data)):
        res += data[i]
    print(res)

solve()