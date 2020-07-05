a=list(input())
print(a)
for i in range(1,len(a)-1):
    if a[i-1]<a[i]<a[i+1]:
        print(i)
    
    
        
        