a1=input()[1:-1].split(',')
a=[int(y) for y in a1]
for i in range(1,len(a)-1):
    b1=a[0:i]
    print(type(b))
    b=[int(y) for y in b1]
    if sorted(b)==b:
        c1=a[i:]
        c=[int(y) for y in c1]
        if sorted(c,reverse=True)==c:
            print(i)
        
    
        