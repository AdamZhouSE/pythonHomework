a1=input()[1:-1].split(',')
a=[int(y) for y in a1]
print(a)
for i in range(1,len(a)-1):
    if a[i-1]<a[i]<a[i+1]:
        print(i)
    
    
        
        