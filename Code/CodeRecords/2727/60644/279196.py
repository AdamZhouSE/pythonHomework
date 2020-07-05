t=int(input())
for i in range(0,t):
    n=int(input())
    a1=input().split()
    a2=input().split()
    for j in range(0,n):
        for k in range(0,n-1):
            if int(a1[k])>int(a1[k+1]):
                a1[k],a1[k+1]=a1[k+1],a1[k]
            if int(a2[k])>int(a2[k+1]):
                a2[k],a2[k+1]=a2[k+1],a2[k]
    arr=[]
    for j in range(0,n):
        arr=arr+[abs(int(a1[j])-int(a2[j]))]
    print(max(arr))
