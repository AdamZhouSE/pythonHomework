dayOfM=[0,31,28,31,30,31,30,31,31,30,31,30,31]
date=list(map(int,input().split('-')))
if date[0]%100==0:
    if date[0]%400==0:
        dayOfM[2]=29
elif date[0]%4==0:
    dayOfM[2]=29
day=0
for i in range(1,date[1]):
    day+=dayOfM[i]
day+=date[2]
print(day)