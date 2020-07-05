arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
count=[]
for i in range(0,len(list)):
    cou=0
    for j in range(i+1,len(list)):
        if list[j]<list[i]:
            cou=cou+1
    count.append(cou)
print(count)