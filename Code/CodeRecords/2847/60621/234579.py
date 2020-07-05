a=int(input())
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
ans=0
for i in range(c[0]-1,c[1]-1):
    ans+=b[i]
print(ans)
