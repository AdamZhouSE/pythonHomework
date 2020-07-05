def bin(a):
    res=a%2
    index=10
    while(int(a/2)!=0):
        a=int(a/2)
        res=res+a%2*index
        index=index*10
    return res
num=int(input())
li=[]
for i in range(num):
    a=bin(int(input()))
    b=str(a)
    times=0
    weizhi=0
    for i in range(len(b)-1,-1,-1):
        if(b[i]=='1'):
            times+=1
            weizhi=len(b)-i
    if(times==1):
        print(weizhi)
    else:
        print(-1)