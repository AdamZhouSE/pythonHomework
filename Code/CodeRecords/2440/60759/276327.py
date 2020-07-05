lst = eval(input())
for i in range(1, len(lst)):
    save = lst[i]
    while lst[i - 1] > save and i >= 1:
        lst[i] = lst[i - 1]
        i -= 1
    lst[i] = save
print(lst)
