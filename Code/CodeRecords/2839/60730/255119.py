m = int(input())
n = []
for i in range(m):
    k = input()
    if k in n:
        print("YES")
    else:
        print("NO")
    n[i] = k