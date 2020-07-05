l=list(map(int,input().split()))
if l[0]==l[1]:print("0 0 0 0 0 0 0 0 0 0",end='')
else:
    s=""
    if l[0]==0:l[0]=1
    for i in range(l[0],l[1]+1):
        s+=str(i)


    rs=""
    for i in range(10):
        count=str(s.count(str(i)))
        if i<9:rs+=count+" "
        else:rs+=count
    print(rs,end='')
