n = int(input())
l = list(map(int, input().split()))
list1 = []
pre = l[0]
temp = 0
for i in range(n):
    if l[i] != pre:
        list1.append(temp)
        temp = 1
        pre = l[i]
    else:
        temp += 1
    if i == n - 1:
        list1.append(temp)
max1 = 0
#print(list1)
for i in range(len(list1)-1):
    temp =list1[i] if list1[i]<list1[i+1] else list1[i+1]
    if max1<temp:
        max1=temp
print(max1 * 2)






