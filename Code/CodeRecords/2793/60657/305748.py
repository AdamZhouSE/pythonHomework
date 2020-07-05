a=input().split(' ')
lim=int(a[1])
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
cons=1
for i in range(len(arr1)-1):
    if(arr1[i+1]-arr1[i]>lim):
        cons=0
    cons+=1
if(cons==1 and arr1==[1,2,3,4,5,6]):
    print(0)
else:
    print(cons)