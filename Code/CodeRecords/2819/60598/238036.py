num = int(input())
count2 = 0
count1 = 0
count3 = 0
car = 0
groups = input().split(" ")
for i in range(len(groups)):
    if groups[i] == "4":
        car += 1
    elif groups[i] == "1":
        count1 += 1
    elif groups[i] == "2":
        count2 += 1
        car += count2//2
        count2 = count2%2
    else:
        count3 += 1
car = car + min(count3, count1)
count1 = count1 - count3
if count1 <= 0:
    car = car - count1 + count2 % 2
else:
    if count2 == 0:
        if count1 % 4 == 0:
            car = car + count1 // 4
        else:
            car = car + count1 // 4 + 1
    else:
        if count1 <= 2:
            car += 1
        else:
            if (count1-2) % 4 ==0:
                car = car + 1 + (count1-2) // 4
            else:
                car = car + 1 + (count1-2) // 4 + 1
print(car)
