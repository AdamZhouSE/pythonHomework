bookings = []
for i in range(0, int(input())):
    bookings.append(list(map(int, input().split(","))))
seats = [0 for i in range(0, int(input()))]
for sub_ls in bookings:
    for i in range(sub_ls[0] - 1, sub_ls[1]):
        seats[i] += sub_ls[2]
print(seats)