def binaryToInt(str):
    result=0
    for i in range(0,len(str)):
        result=result*2+int(str[i])
    return result

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
    str1="1"
    for j in range(1,len(str)):
        if(str1[j-1]==str[j]):
            str1=str1+"0"
        else:
            str1=str1+"1"
    print(binaryToInt(str1))