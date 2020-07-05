def cmp(a, b, c):
    lst1 = [b[0] - a[0], b[1] - a[1]]
    lst2 = [c[0][0] - c[1][0], c[0][1] - c[1][1]]
    return sum(map(lambda x:x ** 2, lst1)) == sum(map(lambda x:x ** 2, lst2))


lst = []
for i in range(4):
    lst.append(list(eval(input())))
for i in range(3):
    lst_c = lst[1:]
    item = lst_c[i]
    lst_c.remove(item)
    if not cmp(lst[0], item, lst_c):
        print('False')
        break
else:
    print('True')
