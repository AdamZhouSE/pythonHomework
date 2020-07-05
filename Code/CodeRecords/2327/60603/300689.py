
str1=input()
num=[i for i in range(len(str1)+1)]
a=[0]*(len(str1))
for j in range(len(str1)):
    if str1[j]=='D':
        a[j]=max(num)
    else:
        a[j]=min(num)
    num.remove(a[j])
print(a+num)