a = [int(i) for i in input().split(',')]
elems = []
for i in a:
    exist = False
    for j in elems:
        if i==j[0]:
            j[1] += 1
            exist = True
            break
    if not exist:
        elems.append([i,1])
no_solution = False
x = elems[0][1]
for i in elems:
    if i[1]<x:
        x = i[1]
for i in elems:
    if i[1]%x!=0:
        no_solution = True
        break
if no_solution or x<2:
    print('False')
else:
    print('True')