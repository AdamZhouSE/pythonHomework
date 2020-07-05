l=int(input())
list0=input().split()
list1=input().split()
list2=[0]*l
count=0
for i in range(l):
    for j in range(l):
        if(list1[i]==list0[j]):
            list2[i]=j
            break
for i in range(l):
    for j in range(i+1,l):
        if list2[i]>list2[j]:
            count+=1
print(count)