n = int(input())
customer = [int(x) for x in input().split()]
customer.sort()
ans = 0
temp = 0
for i in range(0, n):
    j = n - 1
    flag = False
    while j >= i and temp <= customer[j]:
        j -= 1
        flag = True
    if flag:
        j += 1
        ans += 1
        temp += customer[j]
    else:
        break
print(ans)
