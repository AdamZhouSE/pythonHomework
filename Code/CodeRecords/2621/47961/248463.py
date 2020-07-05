a=eval(input())
num=len(a)
max1=-10000000
if num==1:
    print(a[0])
else:
    for i in range(0,num):
        kk=a[i]
        for j in range(i+1,num):
            kk=kk+a[j]
            if kk>max1:
                max1=kk
    print(max1)