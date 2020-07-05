n=int(input())
for i in range(n):
    m=int(input())
    s=input()
    sl=s.split( )
    temp=[]
    for j in sl:
        temp.append(int(j))
    temp.sort()
    #print(temp)
    if(m%2==0):
        t=int((temp[int(m/2)-1]+temp[int(m/2)])/2)
        print(t)
    else:
        print(temp[int(m/2)])