n=int(input())
list=[]
while(n>1):
    list.append(n%2)
    n=int(n/2)
list.append(n)
list.reverse()
for x in range(0,len(list)):
    if(list[x]==1):list[x]=0
    else:list[x]=1
re=0
for i in range(0,len(list)):
    re=re+list[i]*pow(2,len(list)-i-1)
print(re)