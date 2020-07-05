n=int(input())
list4=input().split()
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
t=int(list4[0])
sum=1
for i in range(1,n):
    if int(list4[i])>=t:
        t=t+int(list4[i])
        sum=sum+1
print(sum)