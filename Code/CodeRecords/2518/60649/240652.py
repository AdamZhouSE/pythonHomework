house=input()
heaters=input()
house=list(map(int,house.split(",")))
heaters=list(map(int,heaters.split(",")))
house.sort()
heaters.sort()
min=0
for i in range(len(house)):
    j=0
    while(j<len(heaters)-1) and (abs(heaters[j] - house[i]))>(abs(heaters[j+1]-house[i])):
        j+=1
    min=max(min,abs(heaters[j]-house[i]))
print(min)