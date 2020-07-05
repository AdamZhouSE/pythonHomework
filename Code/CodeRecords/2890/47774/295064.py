#找一个点，毁灭一条直线，不用考虑最少策略
n,x0,y0=map(int,input().split(' '))
res=0
dic={}
for i in range(n):
    x,y=map(int,input().split(' '))
    if x!=x0:
        k=(y-y0)/(x-x0)#斜率
        dic[k]=1
    else:
        res=1
for i in dic:
    res+=dic[i]
print(res)