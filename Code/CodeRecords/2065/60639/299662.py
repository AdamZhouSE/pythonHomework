string=input()
result=''
for i in range(len(string)):
    if string[i]!=' ':
        string=string[i:len(string)]
        break
if (string[0]=='-' or string[0]=='+') or string[0].isdigit():
    result+=string[0]
    for i in range(1,len(string)):
        if string[i].isdigit():
            result+=string[i]
        else:
            break
    if abs(int(result))>2147483648:
        if result[0].isdigit():
            result='2147483648'
        else:
            result=result[0]+'2147483648'
    print(result)
else:
    print(0)