def operationA(booking:[[int]],l,r):
    if not len(booking):
        booking.append([l,r])
        return 0
    res=0
    i=0
    while i<len(booking):
        if booking[i][1]<l:
            i+=1
            continue
        if r<booking[i][0]:
            i+=1
            continue
        res+=1
        booking.remove(booking[i])
    booking.append([l,r])
    return res


n=int(input())
bookings=[]
for _ in range(n):
    ope=input().split()
    if ope[0]=='A':
        l, r = int(ope[1]), int(ope[2])
        print(operationA(bookings,l,r))
        # print(bookings)
    elif ope[0]=='B':
        print(len(bookings))