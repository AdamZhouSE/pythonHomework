number=int(input(""))
list=input("").split(" ")
time=[]
for i in range(number-1):
    time.append(int(list[i]))
list_0=input("").split(" ")
sum=0
for i in range(int(list_0[0]),int(list_0[1])):
    sum=sum+time[i-1]
print(sum)