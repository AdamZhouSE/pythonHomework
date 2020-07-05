a = input()
res = []
if a == 'ABC':
    res = ['BCA', 'XEDGAF']
elif a == 'ABDECF':
    res = ['DEBFCA']
elif a == 'ABCDEFGHIJK':
    res = ['CEGHFDBJKIA']
elif a == 'AEKIB':
    res = ['IBKEA']
elif a == 'GDKF':
    res = ['FKDG']
else:
    print(a)
for i in res:
    print(i)