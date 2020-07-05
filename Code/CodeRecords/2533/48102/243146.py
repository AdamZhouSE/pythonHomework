def sort_2():
    ls = eval(input())
    odd = []
    both = []
    for i in ls:
        if i % 2 == 0:
            both.append(i)
        else:
            odd.append(i)
    return both + odd


print(sort_2())