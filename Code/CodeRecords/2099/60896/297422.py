a=input()
a=a[::-1]
mul=1
count=0
for i in range(0,len(a)):
    count+=(ord(a[i])-64)*mul
    mul*=26
print(count)
