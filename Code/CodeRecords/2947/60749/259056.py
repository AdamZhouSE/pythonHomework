n=int(input())
str1=input()
def link(str1,str2):
    print(str1+str2)
    return str1+str2
def chop(str1,a,b):
    print(str1[a:a+b])
    return str1[a:a+b]
def half(str1,str2,a):

    str1=str1[0:a]+str2+str1[a:]
    print(str1)
    return str1
def search(str1,str2):
    length=len(str2)
    if length==1:
        for x in range(0,len(str1)):
            if str1[x]==str2:
                return x
        return -1

    for x in range(0,len(str1)-length+1):

        if str1[x:x+length]==str2:
            return x
    return -1
res=[]
for h in range(0,n):
    res.append(input().split(" "))
for h in res:
    if h[0]=='1':
        str1=link(str1,h[1])

    elif h[0]=='2':
        str1=chop(str1,int(h[1]),int(h[2]))

    elif h[0]=='3':
        str1=half(str1,h[2],int(h[1]))

    elif h[0]=='4':
        print(search(str1,h[1]))