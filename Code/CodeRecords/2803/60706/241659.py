list=input().split(' ')
n=int(list[0])
m=int(list[1])
num=[]
for i in range(0,n):
    list1=input().split(' ')
    k=int(list1[0])
    for j in range(1,len(list1)):
        num.append(int(list1[j]))
le=len(num)
for i in range(le):
        for j in range(i + 1, le):
            if int(num[i]) >int(num[j]):
                num[i], num[j] = num[j], num[i]
for i in range(0,le):
    for j in range(i+1,le):
        if num[i]==num[j]:
            num[j]=int(0)
count=0
for i in range(le):
    if num[i]!=0:
        count=count+1
str=''
if count>=m:
    str='YES'
else:
    str='NO'
print(str)
