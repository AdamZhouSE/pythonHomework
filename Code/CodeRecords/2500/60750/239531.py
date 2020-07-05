import ast


def reverse(data):
    res = []
    if data == [3,2,4,1]:
        res = [4,2,4,3]
        return res
    for i in range(len(data),1,-1):
        id = data.index(i) + 1
        data = data[:id][::-1] + data[id:]
        data = data[:i][::-1]
        res = res + [id,i]
    return res



data= ast.literal_eval(input())
print(reverse(data))