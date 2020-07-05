n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list2=[]
for i in range(n):
    p=i
    l=1
    if p<n-2:
        while(list1[p]<list1[p+1]):
            l+=1
            p+=1
            if p==n-2 :
                if list1[p]<list1[p+1]:
                    l+=1
                    break
        list2.append(l)    
if len(list2)==0:
    print("1")
else:
    print(max(list2)  )     
        
        