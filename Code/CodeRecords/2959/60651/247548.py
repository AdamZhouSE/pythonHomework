list1=list(input())
list2=list(input())
l1=len(list1)
l2=len(list2)
sum=0
list3=[]
list4=[]
for i in range(l1):
    for j in range(i+1,l1+1): 
        list3.append("".join(list1[i:j]))        

for i in range(l2):
    for j in range(i+1,l2+1):
        list4.append("".join(list2[i:j])) 
      
for i in list4:
    for j in list3:
        if i==j:
            sum+=1
print(sum)        
        