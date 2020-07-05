num = input()[1:-1].split(',')
for i in range (0,len(num)):
    num[i] = int(num[i])

count = []

for i in range(0,len(num)-1):
    temp = 0
    for j in range(i,len(num)):
        if num[i]>num[j]:
            temp+=1
    count.append(temp)

count.append(0)
print(count)