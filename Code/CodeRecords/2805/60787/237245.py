n=int(input())
list=[int(i) for i in input().split()]
max=0
for i in range(0,n):
    temp=0
    for j in range(i,n):
        if j==n-1:
            temp=n-i
        elif list[j]>=list[j+1]:
            temp=j-i+1
            break
    if temp>max:
        max=temp
print(max)