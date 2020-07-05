str=input()
n=int(str[6])
if(int(str[5])==1):
    n+=10
day=0
if(n==1):
    print(str[8:])
if(n==2):
    day=31+int(str[8:])
    print(day)
if((n>2)and(int(str[0:4])%4==0)):
    if(n==3):
        day=60+int(str[8:])
        print(day)
    if (n == 4):
        day = 91 + int(str[8:])
        print(day)
    if (n == 5):
        day = 121 + int(str[8:])
        print(day)
    if (n == 6):
        day = 152 + int(str[8:])
        print(day)
    if (n == 7):
        day = 182 + int(str[8:])
        print(day)
    if (n == 8):
        day = 213 + int(str[8:])
        print(day)
    if (n == 9):
        day = 244 + int(str[8:])
        print(day)
    if (n == 10):
        day = 274 + int(str[8:])
        print(day)
    if (n == 11):
        day = 305 + int(str[8:])
        print(day)
    if (n == 12):
        day = 335 + int(str[8:])
        print(day)
    
else:
    if (n == 3):
        day = 59 + int(str[8:])
        print(day)
    if (n == 4):
        day = 90 + int(str[8:])
        print(day)
    if (n == 5):
        day = 120 + int(str[8:])
        print(day)
    if (n == 6):
        day = 151 + int(str[8:])
        print(day)
    if (n == 7):
        day = 181 + int(str[8:])
        print(day)
    if (n == 8):
        day = 212 + int(str[8:])
        print(day)
    if (n == 9):
        day = 243 + int(str[8:])
        print(day)
    if (n == 10):
        day = 273 + int(str[8:])
        print(day)
    if (n == 11):
        day = 304 + int(str[8:])
        print(day)
    if (n == 12):
        day = 334 + int(str[8:])
        print(day)
