a = list(eval(input()))
sum = 0
for i in range(a.__len__()-1):
    for j in range(i+1,a.__len__()):
        if a[i] > 2*a[j]:
            sum += 1
print(sum) 