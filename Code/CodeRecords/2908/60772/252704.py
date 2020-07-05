n=int(input())         
a=[]                          
for i in range(n):    
    s=input()
    a.append(s)           

for i in range(len(a)):  
    a[i]=sorted(a[i])

count=1
a=sorted(a)               
for i in range(1,len(a)):      
    if a[i]!=a[i-1] :
        count+=1

print(count)             