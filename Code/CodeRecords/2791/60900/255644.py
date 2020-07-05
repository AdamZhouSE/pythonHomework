n = input()
str = input().split(" ")
for i in range (0,int(n)):
    str[i] = int(str[i])

index = []

for i in range(0,int(n)):
    if str[i]==1:
        index.append(i)

result = []
for i in range(1,len(index)):
    result.append(index[i]-index[i-1])

result.append(int(n)-index[len(index)-1])

print(len(index))

for i in range(0,len(result)-1):
    print(result[i],end=' ')

print(result[len(result)-1])
