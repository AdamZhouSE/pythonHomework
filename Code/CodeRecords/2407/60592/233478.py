data = input()
year = int(data[0:4])
month = int(data[5:7])
day = int(data[8:10])
sum = 0
spe = 0
if year % 100 == 0:
    if year % 400 ==0:
        spe = 1
else:
    if year % 4 == 0:
        spe = 1
if month==12:
    sum+=31+28+31+30+31+30+31+31+30+31+30+day
elif month == 11:
    sum += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
elif month == 10:
    sum += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
elif month == 9:
    sum += 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
elif month == 8:
    sum += 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
elif month == 7:
        sum += 31 + 28 + 31 + 30 + 31 + 30 + day
elif month == 6:
    sum += 31 + 28 + 31 + 30 + 31 + day
elif month == 5:
    sum += 31 + 28 + 31 + 30 + day
elif month == 4:
    sum += 31 + 28 + 31 + day
elif month == 3:
    sum += 31 + 28 + day
elif month == 2:
    sum += 31 + day
else:
    sum += day
if spe and month>2:
    sum+=1
print(sum)
