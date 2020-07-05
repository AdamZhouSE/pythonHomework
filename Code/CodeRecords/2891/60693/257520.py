n=int(input())
money=list(map(int,input().split()))
max_money=max(money)
res = 0
for x in money:
    res += max_money-x
print(res)