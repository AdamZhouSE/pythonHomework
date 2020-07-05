t=int(input())
for i in range(t):
    number=input()
    sources=input().split(" ")
    source=[]
    for j in sources:
        source.append(int(j))
    ou=[]
    ji=[]
    for j in source:
        if(j%2==0):
            ou.append(j)
        else:
            ji.append(j)
    res=""
    for j in ou:
        res=res+str(j)+" "
    for j in ji:
        res=res+str(j)+" "
    print(res)