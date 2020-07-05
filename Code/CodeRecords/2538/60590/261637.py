import ast
lists = ast.literal_eval(input())
maxNum = max(lists)

res = 0
if maxNum >= 0:
    print(maxNum+1)
else:
    print(1)