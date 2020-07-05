date=input()
year=int(date[0:4])
month=int(date[5:7])
date=int(date[8:])
flag=False
if (year%4==0 and year%100!=0) or year%400==0 :
    flag=True
days=0
for i in range(1,month):
    if i==1:
        days+=31
    elif i==2:
        if flag:
            days+=29
        else:
            days+=28
    elif i==3:
        days+=31
    elif i==4:
        days+=30
    elif i==5:
        days+=31
    elif i==6:
        days+=30
    elif i==7:
        days+=31
    elif i==8:
        days+=31
    elif i==9:
        days+=30
    elif i==10:
        days+=31
    elif i==11:
        days+=30
days+=date
print(days)