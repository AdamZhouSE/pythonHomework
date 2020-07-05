number=int(input(""))
list_1=input("").split(" ")
source=[]
for i in range(number):
    source.append(int(list_1[i]))
book=int(input(""))
list_2=input("").split(" ")
sign=[]
for i in list_2:
    sign.append(int(i))
sums=[]
for i in range(number):
    sum=0
    for a in range(i+1):
        sum=sum+source[a]
    sums.append(sum)
for i in sign:
    for a in range(len(sums)):
        if(i<=sums[a]):
            print(a+1)
            break
        