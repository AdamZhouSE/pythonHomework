tomatoSlices=int(input())
cheeseSlices=int(input())
a,b=0,0
for i in range(0,tomatoSlices//4+1):
    if 4*i+(cheeseSlices-i)*2==tomatoSlices:
        a,b=i,cheeseSlices-i
if 4*a+b*2==tomatoSlices:print([a,b])
else:print([])