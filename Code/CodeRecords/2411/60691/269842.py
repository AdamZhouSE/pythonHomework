n = int(input())
l =[]
l1 = []

for i in range(0, n):
    l.append(list(map(int, input().split(','))))

for i in range(1, n):
    l1.append((l[i][1]-l[0][1]) / (l[i][0]-l[0][0]))

if l1.count(l1[0]) == n-1:
    print(True)
else:
    print(False)