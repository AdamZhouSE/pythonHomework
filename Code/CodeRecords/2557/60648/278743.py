n=int(input())
for i in range(n):
    m=input()
    ls=[]
    for j in m:
        ls.append(j)
    for k in range(len(ls)-1):
        if ls[k]==ls[k+1]:
            ls[k]='-1'
    for l in range(len(ls)-1):
        if ls[l]=='-1':
            ls.remove(ls[l])
    s="".join(ls)
    print(s)