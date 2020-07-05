order = int(input())
bookings = []
x = 0
while(x<order):
    x+=1
    temp = [int(i) for i in input().split(',')]
    bookings.append(temp)
flights = int(input())
result = [0]*flights
for i in range(order):
	for x in range(bookings[i][0]-1,bookings[i][1]):
		result[x] += bookings[i][2]
print(result)