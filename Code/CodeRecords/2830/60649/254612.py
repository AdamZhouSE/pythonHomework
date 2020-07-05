b,k=map(int,input().split())
a=list(map(int,input().split()))
b%=10
res=0
for i in range(k-1):
    for j in range(k-i-1):
        b*=b
        b%=10
    res+=(b*a[i])%2
res+=a[k-1]%10
if res%2==0:
    print("even")
else:
    print("odd")