source=input("")
a=source[1:-1].split(",")
list=[]
for i in range(len(a)):
    list.append(int(a[i]))
number=int(input(""))
distance=[]
while(len(list)>1):
    for i in range(1,len(list)):
        a=abs(list[i]-list[0])
        distance.append(a)
    list.pop(0)
distance.sort()
print(distance[i-1])