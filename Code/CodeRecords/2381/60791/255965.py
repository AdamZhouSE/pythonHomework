import math
arr1 = [int(i) for i in input().split(',')]
arr2 = [int(i) for i in input().split(',')]
num1 = 0
num2 = 0
for i in range(len(arr1)):
	if(arr1[i]==1):
		num1 += (-2)**(len(arr1)-i-1)
for i in range(len(arr2)):
	if(arr2[i]==1):
		num2 += (-2)**(len(arr2)-i-1)
result = num1 + num2
n = result 
s = []
if(n==0):
    s = [0]
else:
    while(n!=0):
        s.append(int(n%2))
        n = math.ceil((n/(-2)))
s.reverse()
print(s)