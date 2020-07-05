import math
groups = int(input())
people = list(map(int, input().split()))

one = []
two = []
three = []
four = []
for i in range(people.__len__()):
    if people[i]==1:
        one.append(1)
    elif people[i]==2:
        two.append(2)
    elif people[i]==3:
        three.append(3)
    else:
        four.append(4)

cars = 0
cars = cars+four.__len__()

max1 = max(three.__len__(), one.__len__())
if three.__len__() == one.__len__():
    cars = cars+three.__len__()+math.ceil(two.__len__()/2)
else:
    if three.__len__() == max1:
        while one.__len__() > 0:
            three.remove(3)
            one.remove(1)
            cars = cars + 1
        cars = cars + three.__len__() + math.ceil(two.__len__()/2)
    if one.__len__() == max1:
        while three.__len__() > 0:
            one.remove(1)
            three.remove(3)
            cars = cars + 1
        max2 = max(one.__len__(), two.__len__())
        if two.__len__()==0:
            cars = cars+1
        else:
            cars = cars+math.ceil((one.__len__()+two.__len__()*2)/4)

print(cars)