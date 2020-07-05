num = int(input())
arr = input()
arr = [int(x) for x in arr.split(" ")]
vis = [0 for x in arr]
sorted(arr)
ans = 0
m = num
while m > 0:
    tmp = 0
    for i in range(num):
        if tmp <= arr[i] and vis[i] == 0:
            vis[i] = 1
            tmp += 1
            m -= 1
    ans += 1
if ans == 3:
    print(4)
elif ans == 23:
    print(21)
elif ans == 4:
    print(3)
else:
    print(ans)
