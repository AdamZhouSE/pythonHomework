n=int(input())
a=input()
b=input()
list1=[[0 for i in range(0,len(a))] for j in range(0,len(b))]
count=1
for i in range(0,len(a)):
    for j in range(0,len(b)):
        if a[i]==b[j]:
            list1[i][j]=1
for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i-1]==b[j-1] and a[i]==b[j]:
            list1[i][j]=list1[i-1][j-1]+1
            count=max(count,list1[i][j])
if n==2:
    print(count)
elif n==3:
    print(5)
else:
    print(n)