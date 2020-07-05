n=int(input())
b=[int(n) for n in input().split()]
sum=0
a=list(set(b))
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

min1=a[0]
min2=a[1]
max1=a[len(a)-1]
max2=a[len(a)-2]
sum1,sums=0,0
for i in range(0,len(a),2):
    sum1+=b.cout(a[i])*a[i]
for i in range(0,len(b)):
    sums+=b[i]
if sum1>sums-sum1:
    print(sum1)
else:
    print(sums-sum1)

