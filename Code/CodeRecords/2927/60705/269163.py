[n, d] = list(map(int, input().split(" ")))
cases = int(input())
for i in range(0, cases):
    [x, y] = list(map(int, input().split(" ")))
    if x + d >= y >= x - d and - x + d <= y <= - x + 2 * n - d:
        print("YES")
    else:
        print("NO")
