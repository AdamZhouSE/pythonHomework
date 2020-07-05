tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    temp=format(n,'b')
    temp=list(temp)
    for i in range(len(temp)):
        if(temp[i]=='0'):
            temp[i]='1'
        else:
            temp[i]='0'
    while(len(temp)<32):
        temp.insert(0,'1')
    print(int("".join(temp),2))