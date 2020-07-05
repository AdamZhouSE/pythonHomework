nums=input()
num=list(map(int,nums.split(',')))
l1=[]
result=[]
a=0
b=0
for i in range (len(num)):
    l1.append(0)
for i in range(len(num)):
    if num[i]>len(num):
        b=i-num[i]
    else:
        l1[num[i]-1]+=1
for i in range(len(num)):
    if l1[i]==2:
        a=i+1
    if l1[i]==0&b==0:
        b=i+1
result.append(a)
result.append(b)
print(result)