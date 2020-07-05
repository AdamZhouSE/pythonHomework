arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
max,count=0,1
for i in range(0,len(list)):
    pos=i+1
    if pos<len(list):
        if list[pos]>list[i]:
            count=count+1
        else:
            if max<count:
                max=count
            count=1
    else:
        if max<count:
            max=count
print(max)