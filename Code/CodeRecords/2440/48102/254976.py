def sort_insert(ls: list) -> list:
    for i in range(len(ls)-1):
        temp = ls.pop()
        if temp > ls[i]:
            ls.insert(i+1, temp)
        else:
            for j in range(i+1):
                if temp <= ls[j]:
                    ls.insert(j, temp)
                    break
    return ls


lst = eval(input())
print(sort_insert(lst))
