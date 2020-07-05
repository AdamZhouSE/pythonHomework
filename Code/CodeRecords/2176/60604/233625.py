str1=input()
n=len(str1)
a=[0]*n
str=[str1[i] for i in range(n)]
for i in range(n):
    a[i]=i+1;
for i in range(n-1):
    for j in range(n-1,i,-1):
        if str[j]<=str[j-1]:
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
            temp=str[j]
            str[j]=str[j-1]
            str[j-1]=temp
if str[n-1]<=str[n-2]:
    temp=a[n-1]
    a[n-1]=a[n-2]
    a[n-2]=temp
    temp=str[n-2]
    str[n-2]=str[n-1]
    str[n-1]=temp
for i in range(0,n-1):
    print(a[i],end=' ')
print(a[n-1])