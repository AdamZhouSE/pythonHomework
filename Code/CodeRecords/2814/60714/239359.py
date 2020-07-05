n = int(input())
customer = [int(x) for x in input().split()]
customer.sort()
temp = 0
ans = 0
for i in range(0, n):
    if temp <= customer[i]:
        ans += 1
    temp += customer[i]
print(ans)
