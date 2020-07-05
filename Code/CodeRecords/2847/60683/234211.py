n = eval(input())
lst = [int(x) for x in input().split()]
level = [int(x) for x in input().split()]
ans = 0
for i in range(level[0]-1,level[1]-1):
    ans += lst[i]
print(ans)