n = int(input())
num = [int(x) for x in input().split()]
i = 1
ans = []
while i < n:
    temp = 1
    while i < n and num[i] > num[i - 1]:
        temp += 1
        i += 1
    i += 1
    ans.append(temp)
print(max(ans))
