a = input()
count = 0
for i in range(len(a)):
    count += int(a[i])*pow(10,i)
print(count)