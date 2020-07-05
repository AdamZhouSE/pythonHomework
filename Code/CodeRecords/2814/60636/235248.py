number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
sums=[]
for i in range(number):
    sum=0
    for a in range(i+1):
        sum=sum+source[a]
    sums.append(sum)
count=0
for i in range(number):
    if(source[i]<=sums[i]):
        count=count+1
print(count)