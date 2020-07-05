n=int(input())
for i in range(n):
    m=input()
    ls=[]
    for j in m:
        ls.append(int(j))
    for k in range(len(ls)-1):
        if ls[k]==ls[k+1]:
            ls[k]=-1
    for k in range(len(ls)-1):
        if ls[k]==-1:
            ls.remove(ls[k])
    s="".join(ls)
    print(int(s))