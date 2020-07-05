a=input().split(' ')
lim=int(a[1])
arr1=input().split(' ')
arr1=[int(x) for x in arr1]
cons=1
for i in range(len(arr1)-1):
    if(arr1[i+1]-arr1[i]>lim):
        cons=0
    cons+=1
print(cons)