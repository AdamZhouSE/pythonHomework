date=raw_input();
time=date.split('-');
year=int(time[0]);
month=int(time[1]);
day=int(time[2]);
JiLu=0;
if year%400==0:
    JiLu=1;
else:
    if year%4==0 :
        if year%100!=0:
            JiLu=1;
if month == 2:
    day = day + 31;
elif month == 3:
    day = day + 59;
elif month == 4:
    day = day + 90;
elif month == 5:
    day = day + 120;
elif month == 6:
    day = day + 151;
elif month == 7:
    day = day + 181;
elif month == 8:
    day = day + 212;
elif month == 9:
    day = day + 253;
elif month == 10:
    day = day + 283;
elif month == 11:
    day = day + 314;
elif month == 12:
    day = day + 334;
if JiLu==1:
    if month>2:
        day=day+1;
print(day);

