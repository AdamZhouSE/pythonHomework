"""
给你一个按 YYYY-MM-DD 格式表示日期的字符串 date，请你计算并返回该日期是当年的第几天
通常情况下，我们认为 1 月 1 日是每年的第 1 天，1 月 2 日是每年的第 2 天，依此类推
每个月的天数与现行公元纪年法（格里高利历）一致
"""

data=str(input()).split("-")
year=int(data[0])
month=int(data[1])
day=int(data[2])

is_leap=False
if year%4==0 and year%100!=0:
    is_leap=True

month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
if month!=1:
    if is_leap:
        dayth=sum(month_list[0:month-1])+day+1
    else:
        dayth = sum(month_list[0:month-1]) + day
else:
    dayth=day

print(dayth)