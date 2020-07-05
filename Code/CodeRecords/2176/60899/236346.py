'''
a aba ababa ba baba
5  3    1   4   2
'''
a = input()
b = []
str0 = ''
for i in range(len(a)):
    b.append(a[i:len(a)])
strings = [string for string in b]
temp = strings.copy()
strings.sort()
for i in range(len(a)):
    str0 += str(temp.index(strings[i])+1)+" "
print(str0[0:len(str0)-1])


