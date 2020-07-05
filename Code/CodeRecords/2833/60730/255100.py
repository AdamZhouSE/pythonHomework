num = int(input())
m = input().split(" ")
n = list(map(int, m))
j = input().split(" ")
k = list(map(int, j))
k.sort(reverse=True)
if (sum(n) <= k[0]+k[1]):
    print("YES")
else:
    print("NO")
