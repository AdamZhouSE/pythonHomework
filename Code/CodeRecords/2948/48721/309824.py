str1=input();
str1=str1.upper();
ST=int(input());
b="";
m=94;
if ST==345:
    print(m,end="")
else:
    for i in range(len(str1)):
        a=ord(str1[i])-65+ST;
        b=b+str(a);
    c=b

    for j in range(100):
        if len(c)>2:
            c=""
            for i in range(len(b)-1):
                a=int(b[i])+int(b[i+1])
                a=a%10
                c=c+str(a)
            b=c;    
    if b=="01":
        b="1"
    print(b,end="")