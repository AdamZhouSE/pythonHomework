str = input()
str = str[1:-1].split(",")
hour = [int(x[1:3]) for x in str]
minute = [int(x[4:6]) for x in str]
minDiff = 12*60
equal = minDiff
for i in range(len(hour)):
    for j in range(len(hour)):
        if i == j:
            continue
        if hour[i] == hour[j]:
            temp = abs(minute[i]-minute[j])
            if temp < minDiff:
                minDiff = temp
        else:
            if hour[i] > hour[j]:
                temp = 60*(hour[i]-hour[j])+minute[i]-minute[j]
                if temp > equal:
                    temp = 2*equal-temp
                if temp < minDiff:
                    minDiff = temp
            else:
                temp = 60*(hour[j]-hour[i])+minute[j]-minute[i]
                if temp > equal:
                    temp = 2*equal-temp
                if temp < minDiff:
                    minDiff = temp

print(minDiff)
                
