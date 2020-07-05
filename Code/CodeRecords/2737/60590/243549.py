import ast
import math
lists = ast.literal_eval(input())
freq = math.floor(lists.__len__()/3)

sets = set(lists)
arr = list(sets)
res = []
for i in range(arr.__len__()):
    if lists.count(arr[i])>freq:
        res.append(arr[i])

print(res)