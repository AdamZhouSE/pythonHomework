t=int(input())
a=[]
for i in range(t):
    a.append(input())
for i in range(t):
    aa=a[i]
    j=0
    tmp=0
    while True:
        if(j!=len(aa)):
            tmp+=int(aa[j])
            j+=1
        else:
            aa=str(tmp)
            if(len(aa)==1):
                print(aa)
                break
            else:
                j=0
                tmp=0
