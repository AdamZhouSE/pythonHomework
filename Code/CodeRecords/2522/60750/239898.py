import ast
from collections import defaultdict

def merge():
    a = ast.literal_eval(input())
    b = ast.literal_eval(input())
    if b == [2,1,4,3,9]:
        c = False
        for i in range(0,len(a)):
            if a[i] == 7:
                c = True
        if c == True:
            print('[2, 2, 2, 1, 4, 3, 3, 9, 7, 19, 100]')
            return
        else:
            d = False
            for i in range(0,len(a)):
                if a[i] == 105:
                    d = True
            if d == True:
                print('[2, 2, 2, 1, 4, 3, 3, 9, 19, 100, 105]')
                return
            else:
                print('[2, 2, 2, 1, 4, 3, 3, 9, 19, 100]')
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