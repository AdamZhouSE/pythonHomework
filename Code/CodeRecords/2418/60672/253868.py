tomatoSlices=int(input())
cheeseSlices=int(input())
#print(tomatoSlices)
#print(cheeseSlices)
x=tomatoSlices/2-cheeseSlices
y=2*cheeseSlices-tomatoSlices/2
ar=[]
if type(x)==int and type(y)==int:
    ar.append(x)
    ar.append(y)
    print(ar)
else:
    print(ar)