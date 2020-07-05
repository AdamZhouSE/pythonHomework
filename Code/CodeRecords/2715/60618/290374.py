n=eval(input())
if len(n)==1:
    print(0)
else:
    a = [i[0] for i in n]
    b = [i[1] for i in n]
    if len(set(a))+len(set(b))==2*len(n):
        print(len(n))
    else:
        print(len(set(a))+len(set(b))-1)
    
