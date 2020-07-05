class Solution:
    def canculate():
        date = input()
        result = 0
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
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
    canculate()