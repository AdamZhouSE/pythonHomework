destination = int(input())

s1 = input()
s2 = input()

s1 = s1.strip('[]')
s2 = s2.strip('[]')

position = s1.split(',')
speed = s2.split(',')

hour = []

for i in range(len(position)):
    hour.append((destination - int(position[i])) / int(speed[i]))

storage = [[]for i in range(len(position))]

for i in range(len(position)):
    storage[i].append(int(position[i]))
    storage[i].append(float(hour[i]))

ltemp = []
for i in range(len(storage)-1):
    for j in range(i+1, len(storage)):
        if storage[i][0] >= storage[j][0] and storage[i][1] >= storage[j][1]:
            ltemp.append(storage[j])

print(len(storage)-len(ltemp))