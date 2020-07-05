
import ast

def solve():
    a = ast.literal_eval(input())
    b = ast.literal_eval(input())
    res = []
    for i in range(0,len(a)):
        if a[i] in b and a[i] not in res:
            res.append(a[i])
    res.sort()
    print(res)

solve()