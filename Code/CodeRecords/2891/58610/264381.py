input()
money = list(map(int, input().split(' ')))
ceil = max(money)
print(sum([ceil - i for i in money]))