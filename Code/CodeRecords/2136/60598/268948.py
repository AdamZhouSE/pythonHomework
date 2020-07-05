num = int(input())
for i in range(2, num):
    temp = 0
    while temp < num:
        temp = temp * i
        temp += 1
    if temp == num:
        print(i)
        break
