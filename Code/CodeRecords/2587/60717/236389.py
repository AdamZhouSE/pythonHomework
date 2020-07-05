n=int(input())

list2=[]

for i in range(0,n):
    list1=input().split(',')
    list1[0]=int(list1[0])
    list1[1]=int(list1[1])
    list2.append(list1)
    
list1=list2[0]
list2.remove(list1)

count=0

while len(list2)!=0:
    list3=list2[0]
    while list1!=list3:
        if list1[0]<list3[0] and list1[1]<list3[1]:
            count+=1
            list1[0]+=1
            list1[1]+=1
        if list1[0]<list3[0] and list1[1]>list3[1]:
            count+=1
            list1[0]+=1
            list1[1]-=1
        if list1[0]>list3[0] and list1[1]<list3[1]:
            count+=1
            list1[0]-=1
            list1[1]+=1
        if list1[0]>list3[0] and list1[1]>list3[1]:
            count+=1
            list1[0]-=1
            list1[1]-=1
        if list1[0]<list3[0] and list1[1]==list3[1]:
            count+=1
            list1[0]+=1
        if list1[0]>list3[0] and list1[1]==list3[1]:
            count+=1
            list1[0]-=1
        if list1[0]==list3[0] and list1[1]<list3[1]:
            count+=1
            list1[1]+=1
        if list1[0]==list3[0] and list1[1]>list3[1]:
            count+=1
            list1[1]-=1
    list2.remove(list3)
    
print(count)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    