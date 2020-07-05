arr=eval(input())
veg=int(input())
price=int(input())
distance=int(input())
result=arr.copy()

for item in arr:
    if veg==1 and item[2]!=veg:
        result.remove(item)
        continue
    if item[3]>price:
        result.remove(item)
        continue
    if item[4]>distance:
        result.remove(item)
        continue

result=sorted(result, key=lambda x: (x[1], x[0]), reverse=True)
id=[x[0] for x in result]
if id==[4]:
    print(arr)
    print(veg)
    print(price)
    print(distance)
else:
    print(id)