n=int(input())
have=list(input().split(" "))
v=list(input().split(" "))
for i in range(n):
    have[i]=int(have[i])
    v[i]=int(v[i])
v.sort(reverse=True)
num=0
for i in range(n):
    num=num+have[i]
if num>(v[0]+v[1]):
    print("NO")
else:
    print("YES")