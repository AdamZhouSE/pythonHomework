string=input()
index=0
while string[index]==' ':
    index+=1
temp=""
if string[index]=='-':
    temp+="-"
    index+=1
    while index<len(string) and string[index].isdigit():
        temp+=string[index]
        index+=1
    if int(temp)<-2**(31):
        print( -2**(31))
    else:
        print(temp)
elif not string[index].isdigit():
    print(0)
else:
    while index<len(string) and string[index].isdigit():
        temp+=string[index]
        index+=1
    if int(temp)>2**31-1:
        print(2**31-1)
    else:
        print(temp)