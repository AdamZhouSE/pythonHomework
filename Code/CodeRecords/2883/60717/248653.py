list1=input().split()
n=int(list1[0])
m=int(list1[1])
list1=[]
for i in range(0,n):
    list1.append(list(input()))
for i in range(0,n):
    if 'B' in list1[i]:
        a=i
        break
for i in range(0,m):
    if list1[a][i]=='B':
        b=i
        break
count=0
for i in range(0,m):
    if list1[a][i]=='B':
        count+=1
print(a+int((count+1)/2),end=' ')
print(b+int((count+1)/2))