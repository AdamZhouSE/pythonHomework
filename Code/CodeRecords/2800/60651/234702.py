list1=input().split()
list1=[int(x) for x in list1]
n=list1[0]
d=list1[1]
list2=input().split()
list2=[int(x) for x in list2]
sum=0
for i in range(1,n):
    if list2[i]<=list2[i-1]:
        while(list2[i]<=list2[i-1]):
            list2[i]+=d
            sum+=1
print(sum)            
            
