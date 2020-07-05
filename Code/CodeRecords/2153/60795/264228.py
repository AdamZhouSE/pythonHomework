num=int(input())
result=0
th,hu,de,fa=0,0,0,0
mark=0
if num<0:
    num=0-num
    mark=1
if num==10 or num==100 or num==1000 or num==10000:
    result=1
elif num<10:
    result=num
elif num>10 and num<100:
    fa=num%10
    de=num//10
    result=fa*10+de
elif num>100 and num<1000:
    hu=num//100
    de=num%100//10
    fa=num%100%10
    result=fa*100+de*10+hu
elif num>1000 and num<10000:
    th=num//1000
    hu=num%1000//100
    de=num%1000%100//10
    fa=num%1000%100%10
    result=fa*1000+de*100+hu*10+th
if mark==1:
    result=0-result
print(result)


