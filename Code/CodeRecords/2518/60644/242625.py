house=input().split(',')
heater=input().split(',')
r=1
r1=r2=0
isin=False
if int(heater[0])>int(house[0]):
    r1=int(heater[0])-int(house[0])
if int(heater[-1])<int(house[-1]):
    r2=int(house[-1])-int(heater[-1])
if r1>r2:
    r=r1
else:
    r=r2
for i in range(0,len(house)):
    for j in range(0,len(heater)):
        if int(house[i])<=int(heater[j])+r and int(house[i])>=int(heater[j])-r:
            isin=True
            break
    if isin==False:
        r=r+1
        i=i-1
    isin=False
print(r)

