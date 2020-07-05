
import ast

def solve():
    data = ast.literal_eval(input())
    i = 0
    res = 0
    while i < len(data):
        index = []
        for j in range(i,len(data)):
            if data[j] == j and index == []:
                res += 1
                i = i + 1
                break
            else:
                index.append(j)
            satisfied = True
            for k in range(i,j + 1):
                if data[k] not in index:
                    satisfied = False
                    break
            if satisfied:
                res += 1
                break
        i = j + 1
    print(res)

solve()