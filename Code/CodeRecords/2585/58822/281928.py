def all(a):

    res=[]
    n=""
    res.append(a)
    if(("XL" in a)=='False' and ("RX" in a)=='False'):
        return [a]
    for i in range(0,len(a)-1):
        if(a[i]=='X' and a[i+1]=='L'):
            if(i==0):
                n="LX"+a[(i+2):len(a)]
            if (i+1)!=len(a)-1:
                n=a[0:i]+"LX"+a[(i+2):len(a)]
            else:
                n=a[0:i]+"LX"
            li=all(n)
            for k in range(len(li)):
                res.append(li[k])
            i=-1
            return res
        if(a[i]=='R' and a[i+1]=='X'):
            if(i==0):
                n="XR"+a[(i+2):len(a)]
            if (i+1)!=len(a)-1:
                n=a[0:i]+"XR"+a[(i+2):len(a)]
            else:
                n=a[0:i]+"XR"
            li = all(n)
            for k in range(len(li)):
                res.append(li[k])
            i=-1
    return res
n=input()
li=all(n)
res=input()
print(res in li)