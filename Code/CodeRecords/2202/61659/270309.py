T=int(input())

def fillChina(L):
    if L==0:
        return 1
    else:
        res=0
        if L>=2:
            res=res+fillChina(L-1)+fillChina(L-2)
        else:
            res=res+fillChina(L-1)
        return res

for i in range(0,T):
    L=int(input())
    print(fillChina(L))

