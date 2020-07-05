a=input()

flag=1
for i in range(len(a)):
    b=[0:i]
    if b.sort():
        c=[i,len(a)-1]
        if c.sort(reverse=True):
            print(i)
        
        
        