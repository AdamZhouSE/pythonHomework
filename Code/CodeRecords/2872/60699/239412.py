cnt=int(input())
list1=input()
list1=list(list1)
res=0
for i in range(1,len(list1)):
    if list1[i]==list1[i-1]:
        res+=1
print(res)