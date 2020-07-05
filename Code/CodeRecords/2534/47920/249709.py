inp = eval(input())
temp =[]
for i in inp:
    temp = temp + i

for i in range(0,len(temp)):
    for j in range(0,len(temp)):
        if(temp[i]<=temp[j]):
            temp1 = temp[i]
            temp[i] = temp[j]
            temp[j] = temp1
print(temp)