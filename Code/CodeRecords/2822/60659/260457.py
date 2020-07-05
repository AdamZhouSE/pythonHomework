n=int(input())
num1=input().split(" ")
num2=input().split(" ")
k1=int(num1[0])
list1=[]
list2=[]
for i in range(1,k1+1):
	list1.append(int(num1[i]))
k2=int(num2[0])
for i in range(1,k2+1):
	list2.append(int(num2[i]))
winner=-1
counter=0
while len(list1)!=0 and len(list2)!=0 and counter<1000:
	if list1[0]>list2[0]:
		list1.append(list2[0])
		del list2[0]
		list1.append(list1[0])
		del list1[0]
	else:
		list2.append(list1[0])
		del list1[0]
		list2.append(list2[0])
		del list2[0]
	counter+=1
if len(list1)==0:
	winner=2
	print(counter,winner)
elif len(list2)==0:
	winner=1
	print(counter, winner)
else:
	print(winner)