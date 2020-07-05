n=(int)(input())
num=[int(n) for n in input().split()]
yi=0
er=0
for i in num:
    if i==1:
        yi+=1
    if i==2:
        er+=1
zongshu=0
zongshu=zongshu+min(yi,er)
if yi>er:
    zongshu+=(int)((yi-er)/3)
print(zongshu)