a=input()
b=input()
c=input()
list=[]
for i in range(len(a)):
    list1=[]
    list1.append(a[i])
    list1.append(b[i])
    list.append(list1)
result=[]
n=len(list)
def make_profit(start,i):
    if i >=n:
        return 0
    doi_profit=0
    jobi=list[i]
    profiti=int(c[i])
    if int(jobi[0])>=start:
        doi_profit=profiti+make_profit(int(jobi[1]),i+1)
    notdo=make_profit(start,i+1)
    return max(doi_profit,notdo)
res=make_profit(1,0)
print(res)