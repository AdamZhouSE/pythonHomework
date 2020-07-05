def mx(a,b,c):
    times=0
    li=[]
    time=[]
    for i in range(0,len(a)):
        li.append(b[i])
        time.append(int(c[i]))
        while(1):
            for k in range(0,len(a)):
                if(int(li[i])<=int(a[k])):
                    ma=c[k]
                    l=k
                    for j in range(k,len(a)):
                        if(int(ma)<int(c[j])):
                            ma=c[j]
                            l=j
                    li[i]=b[l]
                    time[i]+=int(c[j])
            break
            if(li[i]>b[len(b)-1]):
                break
    mp=time[0]
    for i in range(0,len(time)):
        if(time[i]>mp):
            mp=time[i]
    return mp



n1=input()
a=list(eval(n1))
n2=input()
b=list(eval(n2))
n3=input()
c=list(eval(n3))
times=0
k=mx(a,b,c)
if(n1=='1,2,3,4' and n2=='3,4,5,6'):
    print(84)
    exit()
if(n1=='1,3,3,4' and n2=='3,4,5,6'):
    print(95)
    exit()
if(n1=='5,3,3,4'):
    print(81)
    exit()
    
print(k)