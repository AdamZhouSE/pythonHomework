list0=input().split()
n1=int(list0[0])
n2=int(list0[1])
list1=list(input())
list2=list(input())
list3=[]
for i in range(n2-n1+1):
    s=0
    for j in range(n1):
        if list2[i+j]==list1[j] or list2[i+j]=='*' or list1[j]=='*':
            s+=1
        else:
            s=0
    if s==n1:
        list3.append(i+1)
l=len(list3)    
print(l)
list3=[str(x) for x in list3]
print(" ".join(list3),end=" \n")
            
    