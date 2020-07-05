def binTo_10(str1):
    count=0
    leng=len(str1)
    for i in range(0,leng):
        count=int(str1[i])*pow(2,leng-i-1)+count
    return count
def thrTo_10(str1):
    count = 0
    leng = len(str1)
    for i in range(0, leng):
        count = int(str1[i]) * pow(3, leng - i - 1) + count
    return count
def re(str1,i):
    if(str1[i]=="1"):
        r="0"
    else:
        r="1"
    str2=str1[0:i]+r+str1[i+1:]
    return str2
def fun(str2,i,j):
    if(str2[i]=="0"):
        if(j):
            p="1"
        else:
            p="2"
    elif(str2[i]=="1"):
        if(j):
            p="0"
        else:
            p="2"
    else:
        if(j):
            p="0"
        else:
            p="1"
    str3=str2[0:i]+p+str2[i+1:]
    return str3
str1=input()
str2=input()
list1=[-1]*len(str1)
list2=[-1]*(len(str2)*2)
for i in range(0,len(list1)):
    list1[i]=binTo_10(re(str1,i))
for i in range(0,int(len(list2)/2)):
    list2[2*i]=thrTo_10(fun(str2,i,True))
    list2[2*i+1]=thrTo_10((fun(str2,i,False)))
for num in list1:
    if(num in list2):
        print(num,end="")
        break
    