n=int(input())
fish=list(map(int,input().split()))
maxn=0
for i in range(n-n%2,1,-2):#长度
    for j in range(0,n-i+1):
        l=fish[j]
        r=0
        if l==1:
            r=2
        else:
            r=1
        finded=True
        for k in range(0,i//2):
            if fish[j+k]!=l:
                finded=False
                break
        if finded:
            for k in range(i//2,i):
                if fish[j+k]!=r:
                    finded=False
                    break
        if finded:
            maxn=i
            break
print(maxn)