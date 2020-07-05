n=int(input())
if n==1:
    print(1)
elif n==11:
    print(2)
else:
    s='111'
    while true:
        
        a=int(s)
        if a%n==0:
            print(len(s))
            break
        else:
            s+='1'
    