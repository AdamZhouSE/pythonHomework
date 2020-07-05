a=eval(input())
for i in range(1,len(a)):
    a[0].extend(a[i])
a[0].sort()
print(a[0])