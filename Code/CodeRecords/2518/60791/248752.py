import math
house = [int(i) for i in input().split()]
heater = [int(i) for i in input().split()]
dis = 0
for i in range(len(heater)):
    if(i==0):
        dis = heater[i]-1
    elif(i==len(heater)-1):
        dis = max(dis,len(house)-heater[i])
    else:
        dis = max(dis,int((heater[i]-heater[i-1])/2))
print(math.ceil