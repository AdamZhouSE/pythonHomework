
import ast

def solve():
    data =ast.literal_eval(input())
    data.sort()
    res = 1
    for i in range(0,len(data)):
        if data[i] == res:
            res += 1
        else:
            if data[i] > res:
                break
    print(res)
    
solve()