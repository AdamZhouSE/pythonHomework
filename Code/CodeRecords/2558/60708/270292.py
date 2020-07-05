N=int(input())
for n in range(0,N):
    str=input()
    list=[]
    k=-1
    for item in str:
        if(item=='{'):
            list.append(item)
            k=k+1
        else:
            if(k==-1):
                list.append(item)
                k=k+1
            else:
                if(list[k]=='{'):
                    list.pop(k)
                    k=k-1
                else:
                    list.append(item)
                    k=k+1
    a=0
    b=0
    result=0
    for item in list:
        if item=='{':
            a=a+1
        else:
            b=b+1
    if (a+b)%2==1:
        result=-1
    elif (a+b==0):
        result=0
    else:
        for i in range(0,int((a+b)/2)):
            tempstr=list[i]+list[i+1]
            if(tempstr=='}{'):
                result=result+2
            else:
                result=result+1
    print(result)
