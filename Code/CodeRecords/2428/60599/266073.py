for u in range(int(input())):
    n=int(input())
    s=list(map(int,input().split(' ')))
    ji=[]
    ou=[]
    for i in s:
        if(i%2==0):
            ou.append(i)
        else:
            ji.append(i)
    ou.sort()
    ji.sort()
    ji.reverse()
    res=""
    for i in ji:
        res+=str(i)+" "
    for i in ou:
        res+=str(i)+" "
    print(res)
