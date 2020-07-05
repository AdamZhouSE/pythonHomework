n = input()
str1 = input()
res1 = str1.split(" ")
str2 = input()
res2 = str2.split(" ")
total = 0
max1 = 0
max2 = 0
value = []
input2 = []

for i in range(0,int(n)):
    total=total+int(res1[i])
    value.append(int(res2[i]))

temp = max(value)
index = value.index(temp)
del value[index]
temp = temp + max(value)

if total>temp:
    print("NO")
else:
    print("YES")