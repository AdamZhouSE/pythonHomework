str1=str(input())
str1=str1.strip()
if((str1[0]!="-")&(str1[0]!="+")&(str1.isdigit()==False)):
    print(0)
else:
    xishu=1
    if(str1[0]=="-"):
        xishu=-1
        str1=str1[1:]
    elif(str1[0]=="+"):
        str1=str1[1:]
    i=0
    result=""
    while(i>=0):
        if str1[i].isdigit():
            result=result+str1[i]
            i=i+1
            if i==len(str1):
                break
        else:
            i=-1
    number=int(result)*xishu
    if number>(2**31-1):
        print(2**31-1)
    elif number<(-1*2**31):
        print(-1*2**31)
    else:
        print(number)