def Padovan(n):
    fi=1
    se=1
    th=1
    if 0<=n<=2:
        return 1
    while n-2>0:
        fo = se + fi
        fi = se
        se = th
        th = fo
        n-=1
    return fo
        
n=int(input())
for i in range(n):
    m=int(input())
    print(Padovan(m))