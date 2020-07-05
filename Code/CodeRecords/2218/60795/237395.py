num = raw_input().split(',')
le = len(num)
for k in range(0,le):
    num[k]=int(num[k])
for i in range(0, le):
    for j in range(i + 1, le):
        if num[i] < num[j]:
           num[i], num[j] = num[j], num[i]
a=num[0]*num[1]*num[2] 
print(a)