n = int(input())
money = list(map(int, input().split()))

print(n*max(money)-sum(money))