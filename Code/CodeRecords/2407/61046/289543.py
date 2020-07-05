
def val1(month): # 闰年
    switcher={
        "1":31,
        "2":29,
        "3":31,
        "4":30,
        "5":31,
        "6":30,
        "7":31,
        "8":30,
        "9":31,
        "10":30,
        "11":31,
        "12":31,
    }
    return switcher.get(month)

def val(month):
    switcher={
        "1":31,
        "2":28,
        "3":31,
        "4":30,
        "5":31,
        "6":30,
        "7":31,
        "8":30,
        "9":31,
        "10":30,
        "11":31,
        "12":31,
    }
    return switcher.get(month)

test=list(input())
year=""
month=""
day=""
res=0
for i in range(4):
    year+=test[i]
for i in range(5,7):
    month+=test[i]
for i in range(8,10):
    day+=test[i]
year=int(year)
if(year%4==0 or(year%100==0 and year%400==0)):
    for i in range(1,int(month)):
        d=val1(str(i))
        res+=int(d)
    res+=int(day)
else:
    for i in range(1,int(month) ):
        d = val(str(i))
        res += int(d)
    res += int(day)
print(res)
