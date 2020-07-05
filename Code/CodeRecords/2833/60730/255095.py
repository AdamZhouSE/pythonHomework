num = int(input())
m = input().split(" ")
n = list(map(int, m))
j = input().split(" ")
k = list(map(int, j))
k.sort(reverse=True)
if (sum(n) <= k[len(k)-1]+k[len(k)-2]):
    print("YES")
else:
    print("NO")
