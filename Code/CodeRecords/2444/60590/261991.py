import ast
lists = ast.literal_eval(input())
k = int(input())
t = int(input())

res = "false"
for i in range(lists.__len__()):
    index1 = i
    index2 = i+k
    while index1 < lists.__len__() and index2 < lists.__len__():
        if int(lists[index2]) - int(lists[index1]) == t:
            res = "true"
            break

print(res)
