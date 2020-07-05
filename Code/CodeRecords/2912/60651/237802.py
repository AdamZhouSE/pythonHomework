list1=list(input())
n=len(list1)

list3=[]
for i in range(n-1):
    l=1
    list2=[]
    list2.append(list1[i])
    for j in range(i+1,n):
        list2.append(list1[j])
        set1=set(list2)

        if len(set1)==len(list2):
            l+=1
    list3.append(l)  
print(max(list3))            
        