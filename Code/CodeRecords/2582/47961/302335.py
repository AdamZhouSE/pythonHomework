arr1=[int(i) for i in input().split(',')]
arr2=[int(i) for i in input().split(',')]
maxnum=-100000
for i in range (0,len(arr1)):
    for j in range (0,len(arr1)):
        shuzhi=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
        if shuzhi>maxnum:
            maxnum=shuzhi
print(maxnum)