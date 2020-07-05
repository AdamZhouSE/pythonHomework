s = input()
t = input()
index = -1
m, n = 0, len(t)
try:
    for i in s:
        temp = t.index(i, m, n)
        if temp <= index:
            print('False')
            break
        else:
            index = temp
            m = index + 1
    else:
        print('True')
except ValueError:
    print('False')
