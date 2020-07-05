n = eval(input())
nums = []
ans = 0
last = eval(input())
for i in range(n-1):
    cur = eval(input())
    ans += max(last,cur)
    last = cur
print(ans)