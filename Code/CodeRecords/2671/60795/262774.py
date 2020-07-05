T=int(input())
for i in range(0,T):
    num=int(input())
    max=""
    for j in range(0,num):
        max=max+'1'
    max="0b"+max
    max=eval(max)
    result=0
    if num==1:
        result=0
    elif num==2:
        result=1
    else:
        for j in range(2,max):
            str=bin(j)[2:]
            index=0
            while index<len(str)-1:
                if str[index]=='1' and str[index+1]=='1':
                    result=result+1
                    break
                else:
                    index=index+1
        result=result+1
    print(result)
