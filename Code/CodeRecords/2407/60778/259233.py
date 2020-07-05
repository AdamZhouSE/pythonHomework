str=input()
year=int(str[0:3])
month=int(str[5:7])
day=int(str[8:10])
print("month=",month,"day=",day)
dayInMonth=[31,28,31,30,31,30,31,31,30,31,30,31]
if((year%4==0)^(year%100==0)^(year%400==0)):
    dayInMonth[1]+=1
res=0
for i in range(0,month-1):
    res+=dayInMonth[i]
res+=day
print(res)