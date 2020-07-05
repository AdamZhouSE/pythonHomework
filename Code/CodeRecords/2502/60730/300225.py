num = int(input())
temp, ans = [], 0
for i in range(num):
    temp.append(int(input()))
for j in range(1, num):
    ans += max(temp[j - 1], temp[j])
print(ans)
