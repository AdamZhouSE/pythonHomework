num_m, num_n = map(int, input().split())
m = list(map(int, input().split()))
n = list(map(int, input().split()))
m.sort(reverse=False)
tmp = 0
for i in range(num_n):
    for j in range(num_m):
        if (m[j] <= n[i]):
            tmp = tmp + 1
            if (j == 4):
                print(str(tmp))
                tmp = 0;
            else:
                continue
        else:
            print(str(tmp))
            tmp = 0
            break