def exc(x):
    temp=list(str(bin(x))[2:])
    temp.reverse()
    for i in range(0,len(temp),2):
        if(i==len(temp)-1):
            temp.append('0')
        me=temp[i]
        temp[i]=temp[i+1]
        temp[i+1]=me
    temp.reverse()
    st=''.join(temp)
    return int(st,2)

t=int(input())
for i in range(t):
    print(exc(int(input())))
        