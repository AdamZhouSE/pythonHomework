
import ast

def solve():
    a = ast.literal_eval(input())
    b = ast.literal_eval(input())
    res = []
    for i in range(0,len(a)):
        if a[i] in b:
            res.append(a[i])
            del b[b.index(a[i])]
    res.sort()
    print(res)

solve()
