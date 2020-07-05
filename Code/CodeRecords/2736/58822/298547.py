s=input().split(' ')
arr=input().split(' ')
arr=list(map(int,arr))
for i in range(int(s[1])):
    m=input().split(' ')
    if m[0]=='Q':
        f=arr.copy()
        a1=int(m[1])
        a2=int(m[2])
        a3=int(m[3])
        f=f[a1-1:a2]
        f.sort()
        print(f[a3-1])
    elif m[0]=='C':
        a1 = int(m[1])
        a2 = int(m[2])
        arr[a1-1]=a2