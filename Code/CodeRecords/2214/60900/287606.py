str1 = input()
str2 = input()
a = int(str1[0])
if str1[2]=='-':
    b =-int(str1[3])
else:
    b = int(str1[2])

c = int(str2[0])
if str2[2]=='-':
    d =-int(str2[3])
else:
    d = int(str2[2])

x = a*c-b*d
y = a*d+b*c
print(x,end='')

print("+",end='')
print(y,end='')
print("i")