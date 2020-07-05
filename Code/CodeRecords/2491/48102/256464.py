def same_part(ls1: list, ls2: list) -> list:
    #if len(lst1) > len(lst2):
        #return same_part(lst2, lst1)
    dic1 = {}
    for i in ls1:
        if i not in dic1.keys():
            dic1[i] = ls1.count(i)
    res = []
    for i in ls2:
        if i in dic1.keys() and dic1[i] != 0:
            res.append(i)
            dic1[i] = dic1[i] - 1
    res.sort()
    return res


lst1 = eval(input())
lst2 = eval(input())
print(same_part(lst1, lst2))