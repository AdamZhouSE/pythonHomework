l = input().split(" ")
p = int(l[0])
n = int(l[1])
list1 = []
list2 = []
duplicate = []
for i in range(0,n):
    list1.append(int(input()))
for item in list1:
    temp = item%p
    list2.append(temp)
for i in range(0,n):
    pos = -1
    for j in range(i+1,n):
        if list2[i]==list2[j]:
            pos = j+1
            break
    if(pos >= 0):
        duplicate.append(pos)
if(len(duplicate)>0):
    duplicate.sort()
    print(duplicate[0])
else:
    print(-1)