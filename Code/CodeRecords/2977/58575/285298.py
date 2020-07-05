str=list(input())
res=list()
while str!=list("!"):
    for i in range(str.__len__()):
        if str[i]>='a' and str[i]<='z':
            str[i]=chr(ord('z')-ord(str[i])+ord('a'))
        elif str[i]>='A' and str[i]<='Z':
            str[i]=chr(ord('Z')-ord(str[i])+ord('A'))
    res.append(str)
    str=list(input())
for i in res:
    print (''.join(i))