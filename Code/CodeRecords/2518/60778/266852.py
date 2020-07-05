houses=eval(input())
heater=eval(input())
ptr=0
radius=0
for house in houses:
    if(ptr+1>=len(heater)):
        radius=max(abs(house-heater[ptr]),radius)
    elif(abs(house-heater[ptr])<abs(house-heater[ptr+1])):
        radius=max(abs(house-heater[ptr]),radius)
    else:
        ptr+=1
        radius=max(abs(house-heater[ptr]),radius)
print(radius)