number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
count=0
list=[]
list.append(0)
while(True):
    sum=0
    a=len(list)
    for i in range(len(list)):
        sum=sum+list[i]
    for i in range(number):
        if(source[i]>sum):
            list.append(source[i])
            count=count+1
            break
    if(len(list)==a):
        break
print(count)