line=input()
while(line!='!'):
    temp=list(line)
    for i in range(len(temp)):
        if('a'<=temp[i] and temp[i]<='z'):
            temp[i]=chr(ord('z')-(ord(temp[i])-ord('a')))
        if('A'<=temp[i] and temp[i]<='Z'):
            temp[i]=chr(ord('Z')-(ord(temp[i])-ord('A')))
    print("".join(temp))
    line=input()