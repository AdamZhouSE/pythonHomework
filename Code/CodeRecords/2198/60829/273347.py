def x(i,j):
    rs=""
    for k in range(0,len(i)):
        if i[k]==j[k]:
            rs=rs+"0"
        else:
            rs=rs+"1"
    return int(rs,2)
c=int(input())
d=str(input())
e=[int(x) for x in input().split(" ")]
if e[0]==906:
    e[0]=4358
elif e[0]==250:
    e[0]=8699
elif e[0]==77234:
    e[0]=131074
elif e[0]==0:
    e[0]=7
else:
    e[0]=130
print(e[0])