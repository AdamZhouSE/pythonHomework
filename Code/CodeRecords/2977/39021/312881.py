s = input()
list = []
while(s!='!'):
    list.append(s)
    s=input()
res = []
for c in list:
    str = ''
    for i in c:
        if i>='a' and i<='z':
            str += chr(ord('z') +ord('a')- ord(i))
        elif i>='A' and i<='Z':
            str+= chr(ord('Z') +ord('A')- ord(i))
        else:
            str+= i
    res.append(str)
        
for i in res:
    print(i)