import ast

l=ast.literal_eval(input())
l1 = []
print(l[0])
if l[0] == l[1] or l[1] == l[2] or l[0] == l[2]:
    print(False)
else:
    for i in range(1, 3):
        l1.append((l[i][1] - l[0][1]) / (l[i][0] - l[0][0]))
    if l1.count(l1[0]) == 1:
        print(True)
    else:
        print(False)
