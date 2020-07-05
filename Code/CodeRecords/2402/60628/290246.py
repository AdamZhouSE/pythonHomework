def bookingStatistic(bookings, n):
    answer = [0] * n
    for booking in bookings:
        for k in range(booking[0]-1, booking[1]):
            answer[k] += booking[2]
    return answer

booking_num = int(input())
bookings = []
for i in range(booking_num):
    bookings.append(list(map(int,input().split(','))))
n = int(input())
print(bookingStatistic(bookings, n))