b,k=map(int,input().split())
a=list(map(int,input().split()))
evenodd=0
if b%2==0:
    evenodd=a[k-1]%2
else:
    for i in range(0,k-1):
        evenodd=(evenodd+a[i])%2
    evenodd=(evenodd+a[k-1])%2
if evenodd==1:
    print("odd")
else:
    print("even")