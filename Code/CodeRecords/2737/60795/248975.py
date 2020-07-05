arr1=input()
newarr1=""
for i in range(1,len(arr1)-1):
    newarr1=newarr1+arr1[i]
list=[int(n) for n in newarr1.split(',')]
le=len(list)
re=le%3
sum=(le-re)//3
num=[]
for i in range(0,le):
    count=1
    for j in range(i+1,le):
        if list[j]==list[i]:
            count=count+1
    if count>sum:
        num.append(list[i])
print(num)