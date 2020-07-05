number=int(input(""))
list=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list[i]))
source.sort()
sum_0=0
sum_1=0
if(number%2==0):
    for i in range(int(number/2)):
        sum_0=sum_0+source[i]
    for i in range(int(number/2),number):
        sum_1=sum_1+source[i]
else:
    for i in range(int((number-1)/2)):
        sum_0=sum_0+source[i]
    for i in range(int((number-1)/2),number):
        sum_1=sum_1+source[i]
print(sum_0*sum_0+sum_1*sum_1)