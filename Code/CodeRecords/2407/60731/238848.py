date=input()
year=int(date[0:4])
month=int(date[5:7])
day=int(date[8:])
days=0
if (year%4==0 and year%100!=0) or year%400==0:
    list=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    list=[31,28,31,30,31,30,31,31,30,31,30,31]
if month!=1:
    for i in range(month-1):
        days=days+list[i]
days=days+day
print(days)