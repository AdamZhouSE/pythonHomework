date = str(input())
year = int(date[0:4])
month = int(date[5:7])
day = int(date[8:10])
list1=[0,31,59,90,120,151,181,212,243,273,304,334]
time=list1[month-1]+day    
if month>2 and ((year%400==0 and year!=0) or (year%4==0 and year%100!=0)):
    time = time+1
print(time)
