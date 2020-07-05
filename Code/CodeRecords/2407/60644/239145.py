date=input()
year=int(date[0:4])
month=int(date[5:7])
day=int(date[8:10])
num=0
if (year%4==0 and year%100!=0) or year%400==0:
    if month==1:
        num=day
    elif month==2:
        num=31+day
    elif month==3:
        num=60+day
    elif month==4:
        num=91+day
    elif month==5:
        num=121+day
    elif month==6:
        num=152+day
    elif month==7:
        num=182+day
    elif month==8:
        num=213+day
    elif month==9:
        num=244+day
    elif month==10:
        num=274+day
    elif month==11:
        num=305+day
    else:
        num=335+day
else:
    if month==1:
        num=day
    elif month==2:
        num=31+day
    elif month==3:
        num=60+day-1
    elif month==4:
        num=91+day-1
    elif month==5:
        num=121+day-1
    elif month==6:
        num=152+day-1
    elif month==7:
        num=182+day-1
    elif month==8:
        num=213+day-1
    elif month==9:
        num=244+day-1
    elif month==10:
        num=274+day-1
    elif month==11:
        num=305+day-1
    else:
        num=335+day-1
print(num)