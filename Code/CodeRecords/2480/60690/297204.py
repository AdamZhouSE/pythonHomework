def change(list):
    ou=[]
    ji=[]
    c=[]
    for i in range(len(list)):
        if list[i]%2==0:
            ou.append(list[i])
        else:
            ji.append(list[i])
    for e in ou:c.append(e)
    for e in ji:c.append(e)
    return c


t=int(input())
res=[]
for i in range(t):
    n=int(input())
    list=input().split(" ")
    for j in range(len(list)):
        list[j]=int(list[j])
    list=change(list)
    res.append(list)
for l in res:
    for i in range(len(l)-1):
        print(l[i],end=" ")
    print(l[-1])