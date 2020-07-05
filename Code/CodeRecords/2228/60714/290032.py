target = abs(int(input()))
i = 1
ans = 0
temp = 0
while temp < target:
    temp += i
    i += 1
    ans += 1
if temp == target:
    print(ans)
else:
    ans -= 1
    i -= 1
    if (temp - target) % 2 == 0:
        print(ans + 1)
    else:
        if temp - target > target - temp + i:
            print(ans + 2 * (target - temp + i))
        else:
            print(ans + 2 * (temp - target))
