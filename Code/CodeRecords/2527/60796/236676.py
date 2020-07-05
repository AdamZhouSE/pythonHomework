restaurants=input()
restaurants=restaurants[1:len(restaurants)-1]
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
r=[]
r=restaurants.split("]")
#print(r)
del r[len(r)-1]#删掉最后一个元素的原因：发现最后一个元素是个空的
for i in range(0,len(r)):
    if i==0:
        r[i]=r[i][1:len(r[i])]
    else:
        r[i]=r[i][2:len(r[i])]
    r[i]=r[i].split(",")
    r[i]=[int(x) for x in r[i]]
#print(r)
#下面过滤掉不符合要求的：
for i in range(0,len(r)):
    if i==len(r):
        break
    if (r[i][2]==0 and veganFriendly==1) or (r[i][3]>maxPrice) or (r[i][4]>maxDistance):
         del r[i]
         i=i-1
#print(r)
#下面按ID从高到低排序
for i in range(1,len(r)):
    j=i-1
    while j>=0:
        if r[i][0]<=r[j][0]:
            break
        else:
            j=j-1
    j=j+1#j是r[i]应该插入的位置
    a=r[i]
    del r[i]
    r.insert(j,a)
#print(r)
#下面按rating从高到低排序：
for i in range(1,len(r)):
    j=i-1
    while j>=0:
        if r[i][1]<=r[j][1]:
            break
        else:
            j=j-1
    j=j+1#j是r[i]应该插入的位置
    a=r[i]
    del r[i]
    r.insert(j,a)
#print(r)
result=[]
for i in range(0,len(r)):
    result.append(r[i][0])
print(result)



