date=input()
dateCon=date.split('-')
year=int(dateCon[0])
month=int(dateCon[1])
day=int(dateCon[2])
res=0

if year%4==0 and year%100==0 and year%400!=0:
    month_dayList=[31,28,31,30,31,30,31,31,30,31,30,31]
elif year%4==0:
    month_dayList = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else:
    month_dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for mon in range(month-1):
    res=res+month_dayList[mon]
res=res+day
print(res)