import ast
lists = ast.literal_eval(input())

len = 1
temp = []
for i in range(lists.__len__()-1):
    if lists[i+1]>lists[i]:
        len = len+1
    else:
        temp.append(len)
        len = 1

print(max(temp))