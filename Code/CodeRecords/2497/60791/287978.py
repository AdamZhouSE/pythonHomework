tar = int(input())
posi = eval(input())
speed = eval(input())
m = len(posi)-1
while m>=0 :
    for i in range(m):
        if posi[i] < posi[i+1]:
            temp = posi[i]
            posi[i] = posi[i+1]
            posi[i+1] = temp
            temp = speed[i]
            speed[i] = speed[i+1]
            speed[i+1] = temp
    m-=1
front = 0
count = 1
for i in range(1,len(posi)):
	if(speed[front] == speed[i]):
		if(i==len(posi)-1):
			pass
		else:
			front = i+1
			count += 1
	elif((tar - posi[front])/speed[front] <= (posi[front] - posi[i])/(speed[i]-speed[front])):
		pass
	else:
		if(i==len(posi)-1):
			pass
		else:
			front = i+1
			count += 1
print(count)

            