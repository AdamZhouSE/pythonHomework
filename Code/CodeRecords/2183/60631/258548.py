n = int(input())
data=[]
for j in range(500):
    data.append(j)
for i in range(n):
    m=int(input())
    op=(m-1)*(m)+1
    ed=m*(m+1)+1
    an=0
    for j in range(op,ed):
        an=an+j
    print(an)