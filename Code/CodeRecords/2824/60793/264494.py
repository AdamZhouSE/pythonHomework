temp = list(map(int, input().split()))
t, c = temp[1], temp[-1]
ls = list(map(int, input().split()))
result = 0
for i in range(0, len(ls) - c + 1):
    temp = ls[i:i + c]
    if sorted(temp)[-1] <= t:
        result += 1
print(result)