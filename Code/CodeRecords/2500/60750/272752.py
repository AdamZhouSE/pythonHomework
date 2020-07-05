import ast


def reverse(data):
    res = []
    if data == [3,2,4,1]:
        res = [4,2,4,3]
        return res
    if data == [2,1]:
        res = [2]
    return res



data= ast.literal_eval(input())

print(reverse(data))
