from functools import cmp_to_key
def cmp(x,y):
    if x[1]==y[1]:
        return -1 if x[0]>y[0] else 1
    return -1 if x[1]>y[1] else 1
restaurants=eval(input())
vegan=int(input())
maxPrice=int(input())
maxDistance=int(input())
res=[]
for restaurant in restaurants:
    if restaurant[2]-vegan>=0 and restaurant[3]<=maxPrice and restaurant[4]<=maxDistance:
        res.append(restaurant)
res=sorted(res,key=cmp_to_key(cmp))
final=[]
for item in res:
    final.append(item[0])
print(final)
