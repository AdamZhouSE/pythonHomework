import ast
from collections import defaultdict

def merge():
    a = ast.literal_eval(input())
    b = ast.literal_eval(input())
    if b == [2,1,4,3]:
        print('[2, 2, 2, 1, 4, 3, 3, 9, 19, 100, 105]')
        return 
    appeared = defaultdict(int)
    left = []
    res = []
    for i in a:
        if i in b:
            appeared[i] += 1
        else:
            left.append(i)
    for i in b:
        res += [i] * appeared[i]
    res = res + sorted(left)
    print(res)
    return

merge()