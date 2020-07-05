def ou(list):
    leng=len(list)
    result=0
    for i in range(0,leng):
        if(list[i]%2==0):
            result=result+1
    return result
def ji(list):
    leng=len(list)
    result=0
    for i in range(0,leng):
        if(list[i]%2==1):
            result=result+1
    return result
def minF(a,b):
    if(a>b):
        return b
    else:
        return a
str1=input().split()
n=int(str1[0])
m=int(str1[1])
list1=input().split()
list1=list(map(int,list1))
list2=input().split()
list2=list(map(int,list2))
ou1=ou(list1)
ou2=ou(list2)
ji1=ji(list1)
ji2=ji(list2)
count=minF(ou1,ji2)+minF(ou2,ji1)
print(count)