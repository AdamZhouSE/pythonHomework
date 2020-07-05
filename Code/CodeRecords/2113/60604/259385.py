n=int(input())
def conv(n):
    res=''
    if n>=100:
        #print(n)
        res=conv(n//100)+" Hundred"
        n=n%100
    if n>=20:
        #print(n)
        #print(res)
        tmp=n%10
        if n<30:
            res+=" Twenty"
        elif n<40:
            res+=" Thirty"
        elif n<50:
            res+=" Forty"
        elif n<60:
            res+=" Fifty"
        elif n<70:
            res+=" Sixty"
        elif n<80:
            res+=" Seventy"
        elif n<90:
            res+=" Eighty"
        elif n<100:
            res+=" Ninety"
        res+=conv(n%10)
    elif n==1:
        res+=' One'
    elif n==2:
        res+=' Two'
    elif n==3:
        res+=' Three'
    elif n==4:
        res+=' Four'
    elif n==5:
        res+=' Five'
    elif n==6:
        res+=' Six'
    elif n==7:
        res+=' Seven'
    elif n==8:
        res+=' Eight'
    elif n==9:
        res+=' Nine'
    elif n==10:
        res+=' Ten'
    elif n==11:
        res+=' Eleven'
    elif n==12:
        res+=' Twelve'
    elif n==13:
        res+=' Thirteen'
    elif n==14:
        res+=' Fourteen'
    elif n==15:
        res+=' Fifteen'
    elif n==16:
        res+=' Sixteen'
    elif n==17:
        res+=' Seventeen'
    elif n==18:
        res+=' Eighteen'
    elif n==19:
        res+=' Nineteen'
    return res
tmp=n//1000000000
res=''
if tmp>0:
    res+=conv(tmp)+" Billion"
    n=n%1000000000
tmp=n//1000000
if tmp>0:
    n=n%1000000
    res+=conv(tmp)+" Million"
tmp=n//1000
if tmp>0:
    n=n%1000
    res+=conv(tmp)+" Thousand"
res+=conv(n)
print(res[1:len(res)])































