day = int(input())
sizes = input().split(" ")
sizes = list(map(int,sizes))
if sizes[day-1] == 15:
    print("DOWN")
elif sizes[day-1] == 0:
    print("UP")
else:
    if day==1:
        print(-1)
    elif sizes[day-1]>sizes[day-2]:
        print("UP")
    else:
        print("DOWN")