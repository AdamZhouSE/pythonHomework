tomatoSlices=(int)(input())
cheeseSlices=(int)(input())
result=[]
if((tomatoSlices%2==0)&(tomatoSlices<=4*cheeseSlices)&(tomatoSlices>=2*cheeseSlices)):
    result.append((int)((tomatoSlices-2*cheeseSlices)/2))
    result.append(cheeseSlices-(int)(result[0]))

print(result)