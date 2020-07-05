import json

ar = json.loads(input())
ans = 1
temp = 1
for i in range(len(ar) - 1):
    if ar[i] < ar[i + 1]:
        temp += 1
    else:
        if ans < temp:
            ans = temp
        temp = 1
print(ans)
