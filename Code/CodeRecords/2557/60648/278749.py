n=int(input())
for i in range(n):
    m=input()
    ls=[]
    for j in m:
        ls.append(j)
    for k in range(len(ls)-1):
        if ls[k]==ls[k+1]:
            ls[k]='-1'
    #print(ls)
    '''for o in range(len(ls)):
        if ls[o]=='-1':
            del ls[o]
            o-=1
    '''
    s=""
    for t in range(len(ls)):
        if ls[t]=='-1':
            continue
        else:
            s+=ls[t]
    #s="".join(ls)
    print(s)