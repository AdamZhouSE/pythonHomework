n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
sum=0
list2=[]
for i in range(n):
    if list1[i]==1:
        sum+=1
print(sum)
for i in range(1,n):
    if list1[i]==1:
        list2.append(str(list1[i-1]))
list2.append(str(list1[n-1]))        
print(" ".join(list2))