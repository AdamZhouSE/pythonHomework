arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
result=0
if len(list)<=2:
    result=0
else:
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    for i in range(0,len(list)):
        if i+1<len(list):
            a=list[i+1]-list[i]
            if a>result:
                result=a
        else:
            break
print(result)