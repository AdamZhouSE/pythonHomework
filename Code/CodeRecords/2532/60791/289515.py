a = eval(input())
temp = sorted(a)
count = 0
index = 0
for i in range(len(a)):
    if a[index] <= temp[i] and i<len(a) :
        count+=1
        index = i+1
print(count)