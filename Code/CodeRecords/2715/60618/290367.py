n=eval(input())
if len(n)==1:
    print(0)
else:
    a = [i[0] for i in n]
    b = [i[1] for i in n]
    if len(set(a))+len(set(b))>len(n):
        print(len(set(a))+len(set(b))-1)
    else:
        print(len(n))
    
