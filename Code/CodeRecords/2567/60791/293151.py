a = eval(input())
low = int(input())
up = int(input())
count = 0
for i in range(len(a)):
    temp = 0
    for j in range(i,len(a)):
        temp += a[j]
        if temp >= low  and temp <= up:
            count+=1
print(count)