def atoi(string):
    result=[]
    for i in range(len(string)):
        if i==0:
            if string[i]=='-' or string[i].isdigit():
                result.append(string[i])
            else:
                break
        else:
            if string[i].isdigit():
                result.append(string[i])
            else:
                break
    if len(result)==0:
        return 0
    if len(result)>10:
        return -2147483648
    return int(''.join(result))

a=input()
a=a.replace(' ','')
print(atoi(a))