T=int(input())
bookings=[]
for k in range(T):
    l=list(map(int,input().split(",")))
    bookings.append(l)
n=int(input())
planes=[0 for i in range(n)]
for h in range(T):
    a,b,k=bookings[h]
    for i in range(a-1,b):
        planes[i]+=k
print(planes)