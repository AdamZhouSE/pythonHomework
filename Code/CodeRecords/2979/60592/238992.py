data = input().split(' ')
max = 0
index = 0
for i in range(0,len(data)):
    if len(data[i])>max:
        max = len(data[i])
        index = i
print(data[index])