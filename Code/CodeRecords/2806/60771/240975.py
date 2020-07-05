#23
n = int(input())
day = []
price = []
for i in range(0,n):
    ori = input().split(" ")
    day.append(int(ori[0]))
    price.append(int(ori[1]))
sum = 0
actual = -1
for i in range(0,n):
    if i <= actual:
        continue
    # print("out i: ",i)
    start = i
    flag = False
    while i+1<n and price[i] < price[i+1]:
        i += 1
        flag = True
    actual = i
    for j in range(start,i+1):
        # print("in i: ",i)
        sum += day[j]*price[start]
        # print("sum: ",sum)
    # print("actual: ",actual)
print(sum)