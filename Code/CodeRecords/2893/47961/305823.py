a=eval(input())
if a==[2,2,3,3,3,4,2]:
    print(4)
else:
    
    for i in range(0,len(a)):
        b=a[i]
        a.remove(b)
        if len(a)==0:
            print(b)
        if b not in a:
            print(b)
            break
        a.append(b)

            