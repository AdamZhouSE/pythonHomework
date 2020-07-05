n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    sl=s.split( )
    temp=[]
    for m in sl:
        temp.append(int(m))
    sm=min(temp)
    bi=max(temp)
    if(bi%sm==0):
        print(bi)
    else:
        x=bi
        while (x%bi!=0 or x%sm!=0):
            x=x+1
        print(x)