def trap(height) -> int:
    ans = 0
    h1 = 0
    h2 = 0
    for i in range(len(height)):
        h1 = max(h1,height[i])
        h2 = max(h2,height[-i-1])
        ans = ans + h1 + h2 -height[i]
    return  ans - len(height)*h1

uc = int(input())
ans = list()
for i in range(uc):
    num = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
    t = trap(lists)
    ans.append(t)
for i in ans:
    print(i)