str='YES'
n=int(input())
list=input().split(' ')
list4=input().split(' ')
count=len(list4)
for i in range(count):
        for j in range(i + 1, count):
            if int(list4[i]) >int( list4[j]):
                list4[i], list4[j] = list4[j], list4[i]
sum=int(0)
for i in range(0,len(list)):
    sum=sum+int(list[i])
V=int(list4[n-1])+int(list4[n-2])
if sum>V:
    str='NO'
print(str)
