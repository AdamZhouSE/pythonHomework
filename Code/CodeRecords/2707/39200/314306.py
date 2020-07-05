seats = [int(i) for i in input()[1:-1].split(",")]
cnt = 0
for i in range(0, len(seats), 2):
    if seats[i] // 2 != seats[i + 1] // 2:
        index = seats.index(seats[i] // 2 * 2 + 1 - (seats[i] % 2))
        temp = seats[i + 1]
        seats[i + 1] = seats[index]
        seats[index] = temp
        cnt += 1
print(cnt)
