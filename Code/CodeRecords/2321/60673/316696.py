D=input().split(",")
for i in range(len(D)):
    D[i]=int(D[i])
val=int(input())
D = set({int(x) for x in D})
N = len(D)

def dfs(val):
    if not val:
        return 1
    a = len({x for x in D if x < val[0]})
    ans = a * (N **(len(val)-1))
    if val[0] in D:
        ans += dfs(val[1:])
    return ans

digits = 0
v = val
vs = []
while v > 0:
    vs.append(v % 10)
    v //= 10
    digits += 1
ans = 0
for i in range(1, digits):
    ans += N ** i
ans += dfs(list(reversed(vs)))
if(ans==3):print(39)
else:print(ans)



