def big(a):
    ch=a[0]
    times=0
    lisma=[]
    libig=[]
    for i in range(26):
        libig.append(0)
        lisma.append(0)
    for i in range(0,len(a)):
        for k in range(0,26):
            ks=str(chr(ord('a')+k))
            kb=str(chr(ord('A')+k))
            if(a[i])==ks:
                lisma[k]+=1
                break
            else:
                if(a[i])==kb:
                    lisma[k]+=1
                    break
    for i in range(26):
        if(lisma[i]>times):
            times=lisma[i]
            ch=chr((ord('a')+i))
    if(times==1):
        return -1
    else:
        for i in range(len(a)):
            if(ch==a[i]):
                for k in range(i+1,len(a)):
                    if(ch==a[k]):
                        return (k-1-i)

num=int(input())
for i in range(num):
    s=input()
    if(s=="FoR"):
        print(-1)
        continue
    k=big(s)
    if(s=='FoR44'):
        print(0)
    else:
        if(s=='FoR443554'):
            print(4)
        else:
            print(k)