a = input().split("-")
ans = 0
year = int(a[0])
month = int(a[1])
day = int(a[2])
if year % 4 == 0:
    if month == 1:
        ans = day
    elif month == 2:
        ans = 31 + day
    elif month == 3:
        ans = 60 + day
    elif month == 4:
        ans = 91 + day
    elif month == 5:
        ans = 121 + day
    elif month == 6:
        ans = 152 + day
    elif month == 7:
        ans = 182 + day
    elif month == 8:
        ans = 213 + day
    elif month == 9:
        ans = 244 + day
    elif month == 10:
        ans = 274 + day
    elif month == 11:
        ans = 305 + day
    elif month == 12:
        ans = 335 + day
else:
    day = day - 1
    if month == 1:
        ans = day + 1
    elif month == 2:
        ans = 31 + day + 1
    elif month == 3:
        ans = 60 + day
    elif month == 4:
        ans = 91 + day
    elif month == 5:
        ans = 121 + day
    elif month == 6:
        ans = 152 + day
    elif month == 7:
        ans = 182 + day
    elif month == 8:
        ans = 213 + day
    elif month == 9:
        ans = 244 + day
    elif month == 10:
        ans = 274 + day
    elif month == 11:
        ans = 305 + day
    elif month == 12:
        ans = 335 + day
print(ans)