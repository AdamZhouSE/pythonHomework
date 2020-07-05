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

def exchange(str):
    str1=list(str)
    for i in range(0,7,2):
        temp=str1[i]
        str1[i]=str1[i+1]
        str1[i+1]=temp
    str2=''.join(str1)
    return str2

num=int(input())
for i in range(0,num):
    n=int(input())
    str=intToBinary(n)
    str=exchange(str)
    n1=binaryToInt(str)
    print(n1)