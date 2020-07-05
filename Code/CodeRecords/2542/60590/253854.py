import ast
lists = ast.literal_eval(input())
lists.sort()

len = 1
res = []
for i in range(lists.__len__()-1):
    if int(lists[i+1]) - int(lists[i]) ==1:
        len = len+1
    else:
        res.append(len)
        len = 1
print(max(res))