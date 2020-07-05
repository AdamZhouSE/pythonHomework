n=int(input())
list4=input().split(' ')
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
leng=[]
high=[]
if n%2==0:
    for i in range(int(n/2)):
        leng.append(int(list4[i]))
    for i in range(int(n/2),n):
        high.append(int(list4[i]))
else:
    for i in range(int((n-1)/2)):
        leng.append(int(list4[i]))
    for i in range(int((n-1)/2),n):
        high.append(int(list4[i]))
sum1=0
sum2=0
for i in range(len(leng)):
    sum1=sum1+leng[i]
for i in range(len(high)):
    sum2=sum2+high[i]
ans=sum1*sum1+sum2*sum2
print(ans)
        
