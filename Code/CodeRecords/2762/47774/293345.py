num=int(input())
for nn in range(num):
    n=int(input())
    dct='N'
    x=[0,0]
    li=input().split(' ')
    for i in range(0,2*n,2):
        a=li[i]
        b=int(li[i+1])
        #更改方向
        if a=='R':
            if dct=='N':dct='E'
            elif dct=='E':dct='S'
            elif dct=='S':dct='W'
            elif dct=='W':dct='N'
        elif a=='L':
            if dct=='N':    dct='W'
            elif dct=='E':    dct='N'
            elif dct=='S':    dct='E'
            elif dct=='W':    dct='S'
        elif a=='D':
            if dct=='N':    dct='S'
            elif dct=='E':    dct='W'
            elif dct=='S':    dct='N'
            elif dct=='W':    dct='E'
        
        #更改坐标
        if dct=='N':    x[1]+=b
        elif dct=='E':    x[0]+=b
        elif dct=='S':    x[1]-=b
        elif dct=='W':    x[0]-=b
            
    dis=int((x[0]**2+x[1]**2)**0.5)
    print(dis,dct)
    
    
    
            