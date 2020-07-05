num=(input()).split(" ")
data=(input()).split(" ")
count = 0
for i in range(int(num[0])):
    if int(data[i])<=int(num[1]):
        count = count +1
    else:
        count = count + 2
print(count)