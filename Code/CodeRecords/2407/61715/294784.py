import datetime
class Solution:
    def cancullate():
        date1 = str(input())
        date = date1.replace("-","")
        dd = datetime.datetime.strptime(date, "%Y-%m-%d")
        result = 0
        year = dd.year
        month = dd.month
        day = dd.day
        isLY = 0
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
            isLY = 1
        result += (month - 1) * 30;
        if (month == 2) :
            result += 1
        if (month == 3) :
            result -= 1
        if (month > 5) :
            result += (month - 3) / 2
        result += day
        if (isLY and month != 1) :
            result += 1
        print(result)
    cancullate()