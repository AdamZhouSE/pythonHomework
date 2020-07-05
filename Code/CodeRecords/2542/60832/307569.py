import json

ar = json.loads(input())

ar.sort()
length = len(ar)
index = 1
ans = 1

while index < length:
    temp = 1
    while ar[index] == ar[index - 1] + 1:
        temp += 1
        index += 1

    if temp > ans:
        ans = temp
    index += 1
print(ans)
