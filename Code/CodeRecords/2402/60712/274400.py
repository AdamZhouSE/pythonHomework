allbooking=int(input())
bookings=[]
for i in range(allbooking):
    l=eval(input())
    bookings.append(l)
n=int(input())
result=[0]*n
for i in range(len(bookings)):
    for j in range(bookings[i][0]-1,bookings[i][1]):
        result[j]+=bookings[i][2]
print(result)
        
        