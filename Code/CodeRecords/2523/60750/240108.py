
import ast
from collections import defaultdict


def sortMartix(data):
    row = len(data)
    line = len(data[0])
    temp = defaultdict(list)

    for i in range(0,row):
        for j in range(0,line):
            temp[i - j].append(data[i][j])
    for num in temp:
        temp[num].sort()
    for i in range(0,row):
        for j in range(0,line):
            data[i][j] = temp[i - j].pop(0)
    return data

data = ast.literal_eval(input())
print(sortMartix(data))