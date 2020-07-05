def find(Strlist,n):
    m=int((n+1)/2)
    str=set(Strlist)
    for item in str:
        time=0
        for i in range(0,len(Strlist)):
            if Strlist[i]==item:
                time=time+1
            if(time>=m):
                return  Strlist[i]
    return "-1"


n=int(input())
Str=[""]*n
result=['']*n
for i in range(0,n):
    length=int(input())
    Str[i]=input()
    Strlist=Str[i].split(" ")
    result[i]=find(Strlist,length)
for item in result:
    print(item)