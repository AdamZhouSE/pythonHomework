line1=input().split(" ")
n=int(line1[0])
m=int(line1[1])
line2=input().split(" ")
arr=[]
for i in line2:
	arr.append(int(i))

def switch0(arr,l,r):
	result=sorted(arr[l-1:r])
	counter=0
	for i in range(l-1,r):
		arr[i]=result[counter]
		counter+=1
	return arr

def switch1(arr,l,r):
	result = sorted(arr[l-1:r],reverse=True)
	counter = 0
	for i in range(l-1, r ):
		arr[i] = result[counter]
		counter += 1
	return arr


for i in range(m):
	switch=input().split(" ")
	if int(switch[0])==0:
		arr=switch0(arr,int(switch[1]),int(switch[2]))
	else:
		arr=switch1(arr,int(switch[1]),int(switch[2]))

q=int(input())
print(arr[q-1])