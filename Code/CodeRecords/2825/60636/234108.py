number=int(input(""))
list=[]
for i in range(number):
    list.append(input("").split(" "))
sum=[]
for i in range(number):
    a=int(list[i][0])+int(list[i][1])+int(list[i][2])+int(list[i][3])
    sum.append(a)
smith=sum[0]
a=0
for i in range(number):
    if(sum[i]>smith):
        a=a+1
print(a+1)