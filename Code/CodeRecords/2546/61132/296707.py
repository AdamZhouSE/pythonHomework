def Padovan(n):
    fi=1
    se=1
    th=1
    if 1<=n<=3:
        return 1
    while n-3>0:
        fo = se + fi
        th = fo
        se = th
        fi = se
        n-=1
    return fo
        
n=int(input())
for i in range(n):
    n=int(input())
    print(Padovan(n))