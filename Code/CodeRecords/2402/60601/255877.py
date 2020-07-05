n = eval(input())
bookings = []
for i in range(n):
    bookings.append(list(map(int,input().split(','))))
bookings.sort(key=lambda x:x[0])
n = int(input())
answer = [0]*n
for i in bookings:
    for j in range(i[0],i[1]+1):
        answer[j-1] = answer[j-1] + i[2]
print(answer)