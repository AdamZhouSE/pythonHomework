a=input().split(' ')
n=int(a[0])
m=int(a[1])
b=input().split(' ')
b=list(map(int,b))
b=sorted(b)
zs=0
leng = n
flag = [0]*leng
zzs=0
for i in b:
    if i==0:
        zzs+=1
for i in range(0,leng-1):
        for j in range(i,leng):
            if (b[i]+b[j])==0 and flag[i]!=-1 and flag[j]!=-1:
                flag[i]=-1
                flag[j]=-1
                zs+=1
for i in range(0,m,+1):
    x=input().split(' ')
    y=int(x[0])
    z=int(x[1])
    if z-y+1==1:
        if 0 in b:
            print(1)
        else:
            print(0)
    elif (z-y+1)%2==0:
        if zs>=(z-y+1)//2:
            print(1)
        else:
            print(0)
    else:
        if zs+zzs>=(z-y+1)//2 and zzs>=1:
            print (1)
        else:
            print(0)