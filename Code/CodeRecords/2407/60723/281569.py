temp=input().split('-')
year=int(temp[0])
month=int(temp[1])
day=int(temp[2])
count=0
if year%4==0 and year%100!=0 or year%400==0:
    if month>=3:
        count=count+1
array=[0,31,59,90,120,151,181,212,243,273,304,334]
count=count+array[month-1]+day
print(count)