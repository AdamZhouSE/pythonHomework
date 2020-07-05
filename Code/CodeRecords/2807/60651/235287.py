list1=input().split()
list1=[int(x) for x in list1]
n=list1[0]
m=list1[1]
list2=input().split()
list2=[int(x) for x in list2]
list3=input().split()
list3=[int(x) for x in list3]
sum=0
for i in list3:
    for j in range(n):
        if (i+list2[j])%2==1 and list2[j]>0:
            list2[j]=0
            sum+=1
            break
print(sum)            
            
    