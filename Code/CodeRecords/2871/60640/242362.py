"""
2.19
划分三人团队
"""
n = int(input())
data = map(int, input().split())
amount_two = 0
amount_one = 0
for i in data:
    if i == 1:
        amount_one += 1
    else:
        amount_two += 1
if amount_two >= amount_one:
    print(amount_one)
else:
    print(amount_two+(amount_one-amount_two)//3)
