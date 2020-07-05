n = int(input())
moneys = []
sum = 0
for m in range(0,n):
    c_in = input().split()
    meat = int(c_in[0])
    money = int(c_in[1])
    moneys.append(money)
    sum += meat*min(moneys)
print(sum)