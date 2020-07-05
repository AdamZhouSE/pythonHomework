a=input()
b=input()
str=''
for i in range(len(b)):
    str+=chr(ord(b[i])+int(a)%26)
print(str,end='')