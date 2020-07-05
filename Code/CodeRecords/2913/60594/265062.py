n=(int)(input())
num=[int(n) for n in input().split()]
total=0
for i in num:
    total+=i
if total%2==0:
    print("YES")
else:
    print("NO")