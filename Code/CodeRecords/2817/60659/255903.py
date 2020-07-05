n=int(input())
num=input().split(" ")
for i in range(n):
	num[i]=int(num[i])
result="NO"
for i in range(n):
	target=num[i]
	target2=num[target-1]
	if i+1==num[target2-1] and target!=target2 :
		result="YES"
		break
print(result)