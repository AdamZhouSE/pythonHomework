n = int(input())
shelves = list(map(int, input().split(' ')))
m = int(input())
qs = list(map(int, input().split(' ')))
for i in qs:
    idx = 0
    for j in range(len(shelves)):
        if i <= shelves[j]:
            print(j + 1)
            break
        i -= shelves[j]
