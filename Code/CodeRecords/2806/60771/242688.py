#23
n = int(input())
day = []
price = []
for i in range(0,n):
    ori = input().split(" ")
    day.append(int(ori[0]))
    price.append(int(ori[1]))
all_Sum = 0
minOne = price[0]
for i in range(0,n):
    if minOne <= price[i]:
        price[i] = minOne
    else:
        minOne = price[i]
for i in range(0,n):
    all_Sum += day[i]*price[i]
print(all_Sum)