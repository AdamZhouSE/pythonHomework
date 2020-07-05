import ast
lists = ast.literal_eval(input())

res = 0
for i in range(lists.__len__()-1):
    index = lists.__len__()-1-i
    while index>0:
        if lists[i] > 2*lists[i+index]:
            res = res+1
        index = index-1

print(res)