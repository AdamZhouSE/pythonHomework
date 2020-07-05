n=int(input())
for i in range(0,n):
    tmp=input().split()
    p=int(tmp[0])
    s=int(tmp[1])
    a=(p-(p**2-24*s)**0.5)/12
    v=a*(s/2-a*(p/4-a))
    print('%.5f'%(v))