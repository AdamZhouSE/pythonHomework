ar = list(map(int, input().split(',')))
n = int(input())

ans = None
for i in range(len(ar) - 1):
    for j in range(i + 1, len(ar)):
        if ar[i] + ar[j] == n:
            ans = [i + 1, j + 1]
            print(ans)
            exit()
        elif ar[i] + ar[j] > n:
            break
print(ans)
