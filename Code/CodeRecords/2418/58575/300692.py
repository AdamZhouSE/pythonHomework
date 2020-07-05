tomatoSlices=int(input())
cheeseSlices=int(input())
x=(tomatoSlices-2*cheeseSlices)/2
if x>=0 and x==int(x) and cheeseSlices-x>=0:
    x=int(x)
    print([x,cheeseSlices-x])
else:
    print([])