t=int(input())
while t>0:
    t=t-1
    length=int(input())
    s=input().split()
    ou=[]
    ji=[]
    re=[]
    for item in s:
        if int(item)%2==0:
            ou.append(item)
        else:
            ji.append(item)
    for item in ou:
        re.append(item)
    for item in ji:
        re.append(item)
    result=' '.join(re)+' '
    print(result)