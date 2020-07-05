num = int(input())
m = list(map(int, input().strip().split(" ")))
temp = []
n = int(input())
for j in range(n):
    a, b = map(int, input().strip().split(" "))
    temp = list(set(m[a - 1:b]))
    print(len(temp))
