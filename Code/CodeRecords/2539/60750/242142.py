import ast

def solve():
    data = ast.literal_eval(input())
    tmp = sorted(data)
    res = 0
    left = 0
    for i in range(0,len(tmp)):
        if tmp[i] != data[i]:
            left = i
            break
    right = 0
    for i in range(len(tmp) - 1,-1,-1):
        if tmp[i] != data[i]:
            right = i
            break
    res = right - left + 1
    print(res)
    return

solve()