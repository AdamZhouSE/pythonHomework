date = input()
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])

is_leap = False
if year % 4 == 0 and year % 100 != 0:
    is_leap = True
jan_days, feb_days_leap, feb_days_nonleap, mar_days, apr_days, may_days, jun_days, jul_days, aug_days, sep_days, oct_days, nov_days, dec_days =
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
res = day
for i in range(month-1):
    res+=month_days[i]
# 闰年最后判断，再判断3月之后就加一
if is_leap:
    if month>2:
        res+=1
print(res)