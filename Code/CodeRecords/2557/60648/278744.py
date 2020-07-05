n=int(input())
for i in range(n):
    m=input()
    ls=[]
    for j in m:
        ls.append(j)
    for k in range(len(ls)-1):
        if ls[k]==ls[k+1]:
            ls[k]='-1'
    print(ls)
    for l in ls:
        if l=='-1':
            del l
    s="".join(ls)
    print(s)