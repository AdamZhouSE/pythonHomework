a=input()

flag=1
for i in range(len(a)):
    b=a[0:i]
    if b.sort():
        c=a[i,len(a)-1]
        if c.sort(reverse=True):
            print(i)
        
        
        