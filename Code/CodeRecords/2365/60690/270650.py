num=int(input())
res=[]
for i in range(num):
    n=int(input())
    str=input().split(" ")
    str.sort(reverse=True)
    this=""
    for i in range(n-1):
        if str[i]==str[i+1]+"0":
            temp=str[i]
            str[i]=str[i+1]
            str[i+1]=temp
    for e in str:this+=e
    res.append(this)
for e in res:print(e)