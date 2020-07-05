s=input()
year,month,day=map(int,s.split('-'))
days=[31,28,31,30,31,30,31,31,30,31,30,31]
if(year%4==0) and year%100!=0 or year%400==0:
    days[1]+=1
res=0
for i in range(month-1):
    res+=days[i]
res+=day
print(res)

