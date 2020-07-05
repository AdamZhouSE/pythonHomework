num=int(input())
a=input().split()
for i in range(num):
    a[i]=int(a[i])
b=[]
for i in range(num-1):
    b.append(str(a[i]+a[i+1]))
b.append(str(a[num-1]))
print(' '.join(b))