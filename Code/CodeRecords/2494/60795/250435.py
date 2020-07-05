arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
count=0
for i in range(0,len(list)):
    a=list[i]
    for j in range(i+1,len(list)):
        b=2*list[j]
        if a>b:
            count=count+1
print(count)