# date = "2019-02-10"
date=input()
year=int(date[0:4])
month=int(date[5:7])
day=int(date[8:])
datas=[0,31,28,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or (year%100==0 and year%400==0 ):
    datas[2]=29
sum=0
for i in range(1,month):
    sum+=datas[i]
sum+=day
print(sum)