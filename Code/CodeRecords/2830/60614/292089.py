init=[int(x) for x in input().split()]
b=init[0]
k=init[1]
a=[int(x) for x in input().split()]
sum=0
for i in range(k):
    sum+=a[i]*pow(b,k-1-i)
if sum%2==1:
    print("odd")
else:
    print("even")