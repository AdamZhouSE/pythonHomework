def judge():
    lst = []
    for i in formula:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if len(lst) == 0:
                return 'NO'
            lst.pop()
    return 'YES' if len(lst) == 0 else 'NO'


formula = input()
print(judge(), end='')
