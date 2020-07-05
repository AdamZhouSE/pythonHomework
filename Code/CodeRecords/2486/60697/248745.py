t=int(input())
strs=[]
for i in range(t):
    strs.append(input())
for i in range(t):
    a=strs[i]
    fre=int(a[0])
    l=len(a)
    res=""
    j=1
    while(j<l):

        if(ord(a[j])>=48 and ord(a[j])<=57):
            tm=""
            while(ord(a[j])>=48 and ord(a[j])<=57):
                tm=tm+a[j]
                j+=1
            tm=int(tm)
            s=""
            while a[j]!=']':
                if (ord(a[j]) >= ord('a') and ord(a[j]) <= ord('z')):
                    s=s+a[j]
                j+=1
            for k in range(tm):
                res=res+s
        elif(ord(a[j])>=ord('a') and ord(a[j])<=ord('z')):
            res=res+a[j]
        j+=1
    ans=""

    for i in range(fre):
        ans=ans+res
    print(ans)





