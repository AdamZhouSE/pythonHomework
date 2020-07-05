num = int(input())
point = [1]*num
for i in range(0, num):
    m = []
    m = input().split(" ")
    n = list(map(int, m))
    point[i] = sum(n)
smith = point[0]
point.sort(reverse=True)
print(point.index(smith)+1)