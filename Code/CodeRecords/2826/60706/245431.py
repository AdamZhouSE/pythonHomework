n=int(input())
list4=input().split(' ')
num=[]
for i in range(len(list4)):
    num.append(int(list4[i]))
sum1=0
for i in range(n):
    sum1=sum1+num[i]
i=0
ans=0
count=len(num)
for i in range(count):
    for j in range(i + 1, count):
        if int(num[i]) >int( num[j]):
            num[i], num[j] = num[j], num[i]
sum2=num[0]
for s in range(1,n):
    if num[s]==num[s-1]:
        num[s]=num[s]+1
    elif num[s]<num[s-1]:
        num[s]=num[s]+(num[s-1]-num[s])+1
    sum2=sum2+num[s]
print(sum2-sum1)