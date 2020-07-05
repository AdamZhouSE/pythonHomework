def ss1(r):
    if r==1:
        return 0
    elif r==3:
        return 1
    elif r==5:
        return 2
    elif r==7:
        return 3
    elif r==9:
        return 4
def ss2(r):
    if r==1:
        return 5
    elif r==3:
        return 6
    elif r==5:
        return 7
    elif r==7:
        return 8
    elif r==9:
        return 9
num=int(input())
result=6
if num<9:
    result=num
#1 0   1 1   1 2    1 3   1 4   1 5   1 6   1 7   1 8   1 9   2  0
#10 11 12 13 14 15  16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
elif num>=10 and num<20:
     if num%2==0:
         result=1
     else:
         r=num%10
         if num<20:
             result=ss1(r)
         else:
             result=ss2(r)
elif num>=20 and num<40:
    if num % 2 == 0:
        result = 2
    else:
        r = num % 10
        if num < 30:
            result = ss1(r)
        else:
            result = ss2(r)

print(result)
