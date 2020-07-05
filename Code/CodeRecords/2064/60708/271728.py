# I， V， X， L，C，D和M
str=input()
result=0
k=-1
for item in str:
    if(item=='M'):
        result=result+1000
    if (item == 'D'):
        result = result + 500
    if (item == 'C'):
        result = result + 100
    if (item == 'L'):
        result = result + 50
    else:
        str=str[k+1:]
        break
    k=k+1
if str[0]=='V':
    for item in str:
        if item=='V':
            result=result+5
        else:
            result=result+1
else:
    for item in str:
        if item =='I':
            result=result+1
        elif item=='V':
            result=result+3
        else:
            result=result+8
print(result)