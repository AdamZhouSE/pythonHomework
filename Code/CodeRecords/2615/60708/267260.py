N=int(input())
for n in range(0,N):
    liststr=list(input())
    listresult=[]
    str=liststr[0]
    for i in range(1,len(liststr)):
        str=str+liststr[i]
        if(i==len(liststr)-1):
            listresult.append(str)
            break
        a=ord(liststr[i])-ord(liststr[i-1])
        b=ord(liststr[i+1])-ord(liststr[i])
        if(a!=b):
            listresult.append(str)
            str=liststr[i]
    listlength=[]
    for item in listresult:
        listlength.append(len(item))
    maxlength=max(listlength)
    listpick=[]
    for item in listresult:
        if(len(item))==maxlength:
            listpick.append(item)
    print(sorted(listpick)[len(listpick)-1][::-1])
