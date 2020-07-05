n=int(input())
list=[int(i) for i in input().split()]
sums=0
for i in range(0,n):
    sums+=list[i]
if sums%2==0:
    print("YES")
else:
    print("NO")