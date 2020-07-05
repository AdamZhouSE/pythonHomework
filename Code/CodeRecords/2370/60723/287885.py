num=int(input())
string=''
if num==0:
    string=string+'0'
else:
    while num!=0:
        num,remainder=divmod(num,-2)
        if remainder<0:
            num,remainder=num+1,remainder+2
        string=str(remainder)+string
print(string)