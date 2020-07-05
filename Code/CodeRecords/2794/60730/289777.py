num = int(input())
m = list(map(int, input().split(" ")))
n = int(input())
k = list(map(int, input().split(" ")))
for j in range(len(k)):
    temp = 0
    ans = 0
    for i in range(len(m) + 1):
        if k[j] > temp:
            if i == len(m):
                print(-1)
                break
            temp += m[i]
            ans += 1
        else:
            print(ans)
            break
