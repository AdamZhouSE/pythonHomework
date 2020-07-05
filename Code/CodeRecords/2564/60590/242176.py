lists = list(input().split('],['))

k = int(input())
n = int(input())

sub = []
lists1 = []

for i in range(int(lists[0].__len__()/2)):
    lists1.append(lists[0][2*i+1])

#print(lists1)

for i in range(lists1.__len__()):
    temp = int(lists1[i]) - n
    if temp<0:
        temp = -temp
    sub.append(temp)
#print(sub)

temp = []
for i in range(sub.__len__()):
    temp1 = []
    num = int(lists1[i])
    temp1.append(sub[i])
    temp1.append(num)
    temp.append(temp1)
#print(temp)
temp.sort()

result = []
for i in range(k):
    result.append(int(temp[i][1]))
result.sort()
print(result)