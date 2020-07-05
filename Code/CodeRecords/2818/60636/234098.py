source_1=input("").split(" ")
number=[0]*int(source_1[0])
source_2=input("").split(" ")
for i in range(int(source_1[0])):
	number[i]=int(source_2[i])
number.sort()
sum=0
time=int(source_1[1])
for i in range(0,int(source_1[0])):
	if(time==1):
		sum=sum+number[i]
	else:
		sum=sum+number[i]*time
		time=time-1
print(sum)