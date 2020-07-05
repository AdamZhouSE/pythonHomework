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

def oneAnd(str1,str2):
    str3=""
    for i in range(0,len(str1)):
        if(str1[i]=="1" and str2[i]=="1"):
            str3=str3+"1"
        else:
            str3=str3+"0"
    return str3

num=int(input())
for i in range(0,num):
    n=int(input())
    str1=intToBinary(n)
    list1=list()
    for j in range(n,-1,-1):
        str2=intToBinary(j)
        str3=oneAnd(str1,str2)
        m=binaryToInt(str3)
        flag=True
        for k in range(0,len(list1)):
            if(list1[k]==m):
                flag=False
        if(flag):
            list1.append(m)
    for i in range(0,len(list1)):
        print(list1[i],end=" ")
    print()