def intToBinary(n):
    str=""
    while n>0:
        rem=n%2
        n=n//2
        if rem==1:
            str="1"+str
        else:
            str="0"+str
    count=len(str)
    if count<8:
        for i in range(count,8):
            str="0"+str
    return str

def binaryToInt(str):
    result=0
    for i in range(0,8):
        result=result*2+int(str[i])
    return result

def xOr(str1,str2):
    str3=""
    for i in range(0,len(str1)):
        if(str1[i]==str2[i]):
            str3=str3+"0"
        else:
            str3=str3+"1"
    return str3

num=int(input())
for i in range(0,num):
    n=int(input())
    str=""
    while n>0:
        rem=n%2
        n=n//2
        if rem==1:
            str="1"+str
        else:
            str="0"+str
    num0=0
    num1=0
    for j in range(0,len(str)):
        if(str[j]=="0"):
            num0=num0+1
        else:num1=num1+1
    str1=intToBinary(num0)
    str2=intToBinary(num1)
    str3=xOr(str1,str2)
    print(binaryToInt(str3))