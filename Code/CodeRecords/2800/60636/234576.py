num_d=input("").split(" ")
number=int(num_d[0])
d=int(num_d[1])
list=input("").split(" ")
source=[]
time=0
for i in range(number):
    source.append(int(list[i]))
for i in range(1,number):
    while(source[i]<=source[i-1]):
        time=time+1
        source[i]=source[i]+d
print(time)