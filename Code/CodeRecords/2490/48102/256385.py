def same_part(ls1: list, ls2: list) -> list:
    ls1.sort()
    ls2.sort()
    res = []
    for i in ls1:
        if i in ls2 and i not in res:
            res.append(i)
    res.sort()
    return res


lst1 = eval(input())
lst2 = eval(input())
print(same_part(lst1, lst2))