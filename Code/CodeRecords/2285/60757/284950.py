t=int(input())
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))
    a=[]
    b=[]
    sign=0
    for j in range(1,len(li)):
        if li[j]-li[j-1]<0:
            sign=1
            break
    if(sign==0):
        a.append(0)
        b.append(len(li)-1)
    else:
        sign=1
        for j in range(1,len(li)):
            if sign==1:    
                if li[j]-li[j-1]>0:
                    a.append(j-1)
                    sign=0
            elif sign==0:
                if li[j]-li[j-1]<0:
                    b.append(j-1)
                    sign=1
        if sign==0:
            b.append(len(li)-1)
    for j in range(len(b)-1):
        print('('+str(a[j])+' '+str(b[j])+')',end=' ')
    print('('+str(a[len(b)-1])+' '+str(b[len(b)-1])+')')
                
                