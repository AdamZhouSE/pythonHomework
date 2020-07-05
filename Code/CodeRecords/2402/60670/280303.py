leng=int(input())
bookings=[]
for i in range(0,leng):
    bookings.append(list(map(int,input().split(','))))
n=int(input())
answer=[0 for i in range(0,n)]
for booking in bookings:
    for i in range(booking[0],booking[1]+1):
        answer[i-1]+=booking[2]
print(answer)