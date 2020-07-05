seats = eval(input())

count = 0

for i in range(0, len(seats)):
    if seats[i] % 2 == 0:
        seats[i] = seats[i] // 2
    else:
        seats[i] = (seats[i] - 1) // 2


while len(seats) > 0:
    if seats[0] != seats[1]:
        indexTarget = seats.index(seats[0], 2)
        seats[indexTarget] = seats[1]
        count += 1
        del seats[0]
        del seats[0]
    else:
        del seats[0]
        del seats[0]
print(count)