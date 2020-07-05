def func(c):
    res=''
    for i in range(len(c)-1):
        res = res + str((int(c[i])+int(c[i+1]))%10)
    return res

a = input()
b = int(input())
c = ''
for i in range(len(a)):
    c = c + str(ord(a[i])-ord('A')+b)
for i in range(len(c)-2):
    if c == '100':
        break
    else:
        c = func(c)
print(int(c))