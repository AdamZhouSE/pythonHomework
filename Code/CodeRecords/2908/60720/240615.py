n=int(input())          
a=[]                    
for i in range(n):     
    s=input()
    a.append(s)           

for i in range(len(a)):
    list1=list(a[i])
    for j in range(len(list1)):
        if list1[j]==' ':
            del list1[j]
    list1.sort()
    a[i]=''.join(list1)


ans=1
a.sort()               
for i in range(1,len(a)):
    if a[i]!=a[i-1] :
        ans+=1
print(ans,end='')