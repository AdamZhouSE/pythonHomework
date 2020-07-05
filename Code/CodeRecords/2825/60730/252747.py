num = int(input())
point = [int]
for i in range(0, num-1):
    m = input().split(" ")
    n = list(map(int, m))
    point[i] = sum(n)
smith = point[0]
point.sort(reverse=True)
print(point.index(smith)+1)