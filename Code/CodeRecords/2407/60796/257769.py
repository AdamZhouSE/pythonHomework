date=input().split("-")
year=int(date[0])
month=int(date[1])
day=int(date[2])
m=[31,28,31,30,31,30,31,31,30,31,30,31]
#判断是不是闰年
if year%400==0 or (year%100!=0 and year%4==0):
    m[1]=29

result=0
for i in range(month-1):
    result=result+m[i]
result=result+day
print(result)


