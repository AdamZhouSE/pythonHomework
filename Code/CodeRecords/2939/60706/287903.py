num=[]
num.append(1)
i=0
while(len(num)<500):
    num.append(2*num[i]+1)
    num.append(4*num[i]+5)
    i=i+1
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
str1=input().split(' ')
k=int(str1[0])
m=int(str1[1])
a_s=''
for i in range(k):
    a_s=a_s+str(num[i])
list2=list(a_s)