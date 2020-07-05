def so(li):
    for i in range(0,len(li)-1):
        if i==0 and li[i]>1:
            return 1
        if li[i]<=0 :
            if li[i+1]>0 and li[i+1]!=1:
                return 1
        else:
            if li[i+1]-li[i]==1:
                continue
            else:
                return(li[i]+1)
    return 3
            
a=input()
le = len(a)
a= a[1:le-1]
li = a.split(',')
li = list(map(int,li))
li=sorted(li)
print(so(li))

