nums=list(map(int,input().split('-')))
monthday=[0,31,60,91,121,152,182,213,244,274,305,335]
monthday2=[0,31,59,90,120,151,181,212,243,273,304,334]
year=nums[0]
month=nums[1]
day=nums[2]
res=0
if ((year%4==0) and (year%100!=0)) or (year%400==0):
    res=monthday[month-1]+day
else:
    res = monthday2[month - 1] + day
print(res)
