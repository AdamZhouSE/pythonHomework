inp1 = input().split("[")
temp1 = inp1[1].split("]")
temp2 = temp1[0].split(",")
for i in range(len(temp2)):
    temp2[i] = int(temp2[i])
temp2.sort()
print(temp2)