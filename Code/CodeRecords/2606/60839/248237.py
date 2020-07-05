p = input()
target = int(input())
z = p[1:(len(p)-1)]
x = list(map(int,z.split(",")))

ans=-1
for i in range(0,len(x)):
    if x[i]==target:
        ans=i
print(ans)