lst0=input().split()
n=int(lst0[0])
s=int(lst0[1])
list0=[0]*n;
for i in range(n):
    list0[i]=int(input())
for i in range(n):
    isF=False
    for j in range(0,n,2):
        k=(n-i-j)//2
        a1=0
        a2=0
        for m in range(k):
            a1+=list0[i+m]
            a2+=list0[i+k+m]
        if a1<=s and a2<=s:
            isF=True
            print(k*2)
            break
    if not isF:
        print(0)
