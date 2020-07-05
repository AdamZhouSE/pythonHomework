b,k=map(int,input().split(" "))
lis=list(map(int,input().split(' ')))
n=0
for i in range(0,k):
    n=n+lis[i]*int(pow(b,k-i-1))
if(n%2==0):
    print("even")
else:
    print("odd")