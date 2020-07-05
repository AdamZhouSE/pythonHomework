import ast
lists = ast.literal_eval(input())

res = 0
for i in range(lists.__len__()):
    sets = set(lists)
    arr = list(sets)
    index = 0
    while index!=lists.__len__()-1:
        if lists.count(int(arr[index]))==1:
            res = int(arr[index])
            break
        else:
            index = index+1
print(res)