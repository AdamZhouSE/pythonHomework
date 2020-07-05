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

def hasOne(list,n):
    for i in range(0,len(list)):
        if(list[i][n]=="1"):
            return True
    return False

num=int(input())
for i in range(0,num):
    n,m=map(int,input().split())
    list1=list(map(int,input().split()))
    list2=list()
    list3=list()
    for j in range(0,n):
        if(list1[j]%m==0):
            list2.append(list1[j])
    for p in range(0,len(list2)):
        list3.append(intToBinary(list2[p]))
    str=""
    for k in range(0,8):
        if(hasOne(list3,k)):
            str=str+"1"
        else:
            str=str+"0"
    number=binaryToInt(str)
    print(number)
    