s=input().replace(" ","")
if s[0]!='-'and not s[0].isdigit():
    print(0)
else:
    str=''
    k=0
    for item in s:
        if item =='-'and k==0:
            str=str+item
        elif item.isdigit():
            str=str+item
result=int(str)
if(result>2147483649):
    print(2147483649)
elif(result<-2147483648):
    print(-2147483648)
else:
    print(result)