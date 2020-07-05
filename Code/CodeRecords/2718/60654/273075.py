a = list(input())
b = list(eval(input()))
for i in b:
    temp = a[i[0]]
    a[i[0]] = a[i[1]]
    a[i[1]] = temp
s = ""
for i in a:
    s += i
print(s)    