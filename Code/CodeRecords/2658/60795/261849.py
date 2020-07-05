T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    num,x=arr[0],arr[1]
    A=[int(n) for n in input().split(' ')]
    re=[]
    res=-1
    for j in range(0,num):
        if A[j]%x==0:
            re.append(A[j])
    if len(re)==0:
        res=0
    elif len(re)==1:
        res=re[0]
    else:
        max=0
        for j in range(0,len(re)):
            re[j]=bin(re[j])
            re[j]=re[j][2:]
            le=len(re[j])
            if max<le:
                max=le
        for j in range(0,len(re)):
            if len(re[j])<max:
               oo=max-len(re[j])
               while oo>0:
                   re[j]='0'+re[j]
                   oo=oo-1
        str=""
        index=0
        while index<max:
            mark=0
            for k in range(0,len(re)):
                if re[k][index]=='1':
                    mark=1
                    str=str+'1'
                    break
            if mark==0:
                str=str+'0'
            index=index+1
        res="0b"+str
        res=eval(res)
    print(res)


