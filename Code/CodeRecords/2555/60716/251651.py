num = int(input())
strs = input().split()
lists = [int(i) for i in strs]
index = 0
for i in range(num):
    temp1 = lists[i]
    for j in range(i+1,num):
        temp2 = lists[j]
        for k in range(j+1,num):
            temp3 = lists[k]
            if lists[i]<lists[j] and lists[j]<lists[k]:
                index+=1
print(index)