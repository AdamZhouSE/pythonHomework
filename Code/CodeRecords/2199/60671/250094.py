str1=input()
list1=[]
for x in range(len(str1)):
    for i in range(len(str1) - x):
        list1.append(str1[i:i + x + 1])
list1.sort()
length=len(list1)
temp=1
count=1
lencount=[0]*100
for i in range(length-1):
    if(list1[i]==list1[i+1]):
        temp+=1
    else:
        if(lencount[len(list1[i])]<=temp):
            lencount[len(list1[i])]=temp
        temp=1
ii=max(*lencount)
print(ii)