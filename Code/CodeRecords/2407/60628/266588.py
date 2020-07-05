def dayOfYear(date):
    numOfDay = [31,28,31,30,31,30,31,31,30,31,30,31]
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])
    for i in range(month-1):
        day += numOfDay[i]
    return day + 1 if(isLeapYear(year) and month >= 3) else day

def isLeapYear(year):   
    if (year % 4 == 0 and year % 100 != 0):
        return True
    if (year % 100 == 0 and year % 400 == 0):
        return True
    return False

date = input()
print(dayOfYear(date))