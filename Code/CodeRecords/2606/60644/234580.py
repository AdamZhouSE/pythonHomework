a=input()
a=a[1:-1].split(',')
b=input()
result=-1
for i in range(0,len(a)):
    if a[i]==b:
        result=i
print(result)