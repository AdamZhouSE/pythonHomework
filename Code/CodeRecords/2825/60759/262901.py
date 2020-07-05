n = int(input())
grade = sum(list(map(int, input().split(' '))))
rank = 1
for i in range(n - 1):
    g = sum(list(map(int, input().split(' '))))
    if g > grade:
        rank += 1
print(rank)
