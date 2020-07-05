n = int(input())
boys = input().split(" ")
boys = [int(i) for i in boys]
boys.sort()
m = int(input())
girls = input().split(" ")
girls = [int(j) for j in girls]
girls.sort()
p, q, count = 0, 0, 0
while p < n and q < m:
    if abs(boys[p] - girls[q]) <= 1:
        count += 1
        p += 1
        q += 1
    elif boys[p] < girls[q]:
        p += 1
    elif girls[q] < boys[p]:
        q += 1
print(count)