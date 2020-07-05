a=input()

flag=1
for i in range(len(a)):
    b=eval(a[0:i])
    if b.sort():
        c=eval(a[i,len(a)-1])
        if c.sort(reverse=True):
            print(i)
        
        
        