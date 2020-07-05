m = int(input())
n = [1]*m
for i in range(m):
    k = input()
    if k in n:
        print("YES")
    else:
        print("NO")
    n[i] = k