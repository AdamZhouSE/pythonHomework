a=input().split(',')
for i in range(len(a)):
    a[i]=int(a[i])
#print(a)
b=int(input())
#print(b)
if b<=a[0]:
    print(0)
elif b>a[-1]:
    print(len(a))
else:
    for i in range(1,len(a)):
        if a[i]==b:
            print(i)
        elif a[i-1]<b and a[i]>b:
            print(i)