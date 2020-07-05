num = [int(i) for i in input("")[1 : -1].split(',')]
num = sorted(num)

ans = 0
for i in range(1, len(num)) :
    if num[i] - num[i-1] > ans :
        ans = num[i] - num[i-1]

print(ans)
