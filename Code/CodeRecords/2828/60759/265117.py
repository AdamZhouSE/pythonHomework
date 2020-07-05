n = int(input())
lst = list(map(int, input().split(' ')))
lst.append(0)
lst.sort()
money = 0
for i in range(1, n + 1):
    money += lst[i] - lst[i - 1]
print(money)
