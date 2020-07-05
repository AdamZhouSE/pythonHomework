str1 = input()
str2 = input()
a = int(str1[0])
if str1[1]=='-':
    b =-int(str1[2])
else:
    b = int(str1[2])

c = int(str2[0])
if str2[1]=='-':
    d =-int(str2[2])
else:
    d = int(str2[2])

x = a*c-b*d
y = a*d+b*c
print(x,end='')
if y<0:
    print(y,end='')
else:
    print("+",end='')
    print(y,end='')
print("i")