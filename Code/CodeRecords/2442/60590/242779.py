import ast
lists = ast.literal_eval(input())

lists.sort()
if lists.__len__()<2:
    print(0)
else:
    res = []
    for i in range(lists.__len__()-1):
        temp = lists[i]-lists[i+1]
        temp = abs(temp)
        res.append(temp)
    #print(res)
    res.sort()
    sets = set(res)
    result = list(sets)
    print(result[result.__len__()-1])