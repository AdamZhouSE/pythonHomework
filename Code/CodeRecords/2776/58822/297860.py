n=input()
l=list(eval(n))
l.sort(key=lambda x:len(x))
li=l.copy()
for i in range(len(li)-1,-1,-1):
    s=l[i]
    flag=0
    for k in range(0,len(li)):
        if(l[k] in s and k!=i):
            li[k]=0
            flag=flag+len(l[k])
    if(flag==0):
        li[i]=0
li=[i for i in li if i !=0]
li.sort()
print(li)