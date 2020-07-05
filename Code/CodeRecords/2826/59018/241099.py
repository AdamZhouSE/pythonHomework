n=int(input())
info=input().split(' ')
a=[int(y) for y in info]

a.sort()
count=0
for i in range(n-1):
    if a[i+1]==a[i]:
        a[i+1]=a[i+1]+1
        count=count+1
if a[-2]==a[-1]:
    count=count+1
print(count)
        