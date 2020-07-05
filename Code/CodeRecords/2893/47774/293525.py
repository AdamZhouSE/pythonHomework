num=eval(input())
tmp = []
try:
    for i in num:
        if i not in tmp:
            tmp.append(i)
        else:
            tmp.remove(i)
    print(tmp[0])
except IndexError:
    print('WRONG')
    print(num)
