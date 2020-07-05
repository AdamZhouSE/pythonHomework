n=int(input())
bookings=[[0]*3]*n
for i in range(0,n):
    bookings[i]=[int(k) for k in input().split(",")]
flight=int(input())
re=[0]*flight
for i in range(0,n):
    for j in range(bookings[i][0]-1,bookings[i][1]):
        re[j]+=bookings[i][2]
print(re)
