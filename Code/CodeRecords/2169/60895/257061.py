t=int(input())
while t>0:
    t=t-1
    s=list(input())
    temp=[]
    temp.append(s[0])
    temp.append(s[1])
    s=s[2:]
    for item in s:
        if item>='0' and item<='9':
            temp.append(item)
        elif item=='+':
            x=int(temp[len(temp)-2])+int(temp[len(temp)-1])
            del temp[len(temp)-1]
            del temp[len(temp)-1]
            temp.append(str(x))
        elif item=='-':
            x=int(temp[len(temp)-2])-int(temp[len(temp)-1])
            del temp[len(temp)-1]
            del temp[len(temp)-1]
            temp.append(str(x))
        elif item=='*':
            x=int(temp[len(temp)-2])*int(temp[len(temp)-1])
            del temp[len(temp)-1]
            del temp[len(temp)-1]
            temp.append(str(x))
        elif item=='/':
            x=int(temp[len(temp)-2])/int(temp[len(temp)-1])
            del temp[len(temp)-1]
            del temp[len(temp)-1]
            temp.append(str(x))
        else:
            continue
    print(int(temp[0]))