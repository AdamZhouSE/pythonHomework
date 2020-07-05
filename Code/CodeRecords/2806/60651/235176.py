n=int(input())
needlist=[]
pricelist=[]
sum=0
for i in range(n):
    list1=input().split()
    list1=[int(x) for x in list1]
    needlist.append(list1[0])
    pricelist.append(list1[1])
for p in range(n-1):
    sum+=needlist[p]*pricelist[p]
    if pricelist[p]<=pricelist[p+1]:
        pricelist[p+1]=pricelist[p]
sum=sum+needlist[n-1]*pricelist[n-1]
print(sum)
        