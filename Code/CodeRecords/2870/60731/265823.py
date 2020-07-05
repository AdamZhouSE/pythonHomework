n=int(input())
data=list(map(int,input().split()))
data.sort()
total=0
for i in range(n):
    total+=data[i]
if total%2==0:
    print(total)
else:
    for j in range(n):
        total-=data[j]
        if total%2==0:
            print(total)
            break