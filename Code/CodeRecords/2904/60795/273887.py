n=int(input())
neg=0
if n<0:
    neg=1
    n=0-n
th,hu,de,fa=0,0,0,0
re=0
if n<10:
    re=n
elif n>=10 and n<100:
    de=n//10
    fa=n%10
    re=fa*10+de
elif n>=100 and n<1000:
    hu=n//100
    de=n%100//10
    fa=n%100%10
    re=fa*100+de*10+hu
elif n>=1000:
    th=n//1000
    hu=n%1000//100
    de=n%1000%100//10
    fa=n%1000%100%10
    re=fa*1000+de*100+hu*10+th
if neg==1:
    re=0-re
print(re)
    
