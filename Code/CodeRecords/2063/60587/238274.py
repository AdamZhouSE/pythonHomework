a = input()
b = a
lst1 = list(a)
lst1.reverse()
na = ''.join(lst1)
if na == b:
    print('True')
else:
    print('False')
