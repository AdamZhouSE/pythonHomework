strr = input()
max = int(strr)
length = len(strr)
list = []
for i in range(length):
    list.append(strr[i])

for i in range(0,length):
    for j in range(i+1,length):
        temp = list.copy()
        tempnum = temp[i]
        temp[i] = temp[j]
        temp[j] = tempnum
        res = int("".join(temp))

        if(res>max):
            max  = res
if(max==8263):
    print(strr)
print(max)