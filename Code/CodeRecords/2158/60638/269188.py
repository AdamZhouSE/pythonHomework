num=input().lstrip()
string=""
if num[0]=='-':
    string="-"
    num=num[1:]
if num[0]<"0" or num[0]>"9":
    print(0)
else:
    i=0
    while i <len(num) and num[i]>="0" and num[i]<="9":
        string=string+num[i]
        i=i+1
    if string[0]=="-":
        y="-"
        x=string[1:]
    else:
        y=""
        x=string
    if len(x)>=10 and x>"2147483648":
        if y=="":
            print(int("2147483647"))
        else:
            print(int("-2147483648"))
    else:
        num=int(string)
        print(num)