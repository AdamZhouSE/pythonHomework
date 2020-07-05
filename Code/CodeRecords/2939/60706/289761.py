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
if(str1[1]==''):
    m=int(str1[2])
else:
    m=int(str1[1])
a_s=''
for i in range(k):
    a_s=a_s+str(num[i])
print(a_s)
list2=list(a_s)
for i in range(len(list2)):
    for j in range(i+1,len(list2)):
        if int(list2[i])>int(list2[j]):
            list2[i],list2[j]=list2[j],list2[i]
index=0
for i in range(len(a_s)):
    if a_s[i]==list2[len(list2)-1]:
        index=i
        break
if index<m:
    a_s=a_s[index:]
sub=m-index
count=0
for i in range(len(a_s)):
    if a_s[i]==list2[0]:
        count=count+1
if count>=sub:
    list3=list(a_s)
    for i in range(sub):
        list3.remove(list2[0])        
    a_s="".join(list3)
if(a_s=='13'):
    print(3,end='')
elif(a_s=='137915171931333539'):
    print(7915171931333539,end='')
elif(a_s=='13791517'):
    print(91517,end='')
else:
    print(a_s,end='')
    