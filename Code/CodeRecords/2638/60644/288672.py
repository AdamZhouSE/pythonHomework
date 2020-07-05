e=input().split()
N=int(e[0])
M=int(e[1])
a=input().split()
for i in range(0,N):
    a[i]=int(a[i])
for i in range(0,M):
    s=input().split()
    if s[0]=='1':
        for j in range(int(s[1])-1,int(s[2])):
            a[j]=a[j]+int(s[3])
    elif s[0]=='2':
        res=0
        for j in range(int(s[1])-1,int(s[2])):
            res=res+a[j]
        res=res/(int(s[2])+1-int(s[1]))
        print('%.4f'%res)
    else:
        res = 0
        for j in range(int(s[1]) - 1, int(s[2])):
            res = res + a[j]
        res = res / (int(s[2]) + 1 - int(s[1]))
        ans=0
        for j in range(int(s[1]) - 1, int(s[2])):
            ans=ans+(a[j]-res)*(a[j]-res)
        ans=ans/(int(s[2])+1-int(s[1]))
        print('%.4f'%ans)
