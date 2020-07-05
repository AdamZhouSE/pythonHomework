def hash():
    A=eval("["+input()+"]")
    B=eval("["+input()+"]")
    C=eval("["+input()+"]")
    D=eval("["+input()+"]")
    sumAB=[]
    res=0
    for a in A:
        for b in B:
            if a+b not in sumAB:
                sumAB.append(a+b)

    sumAB.sort()
    for c in C:
        for d in D:
           if -(c+d) in sumAB:
               res+=1
    if res==1:
        print(A)
        print(B)
        print(C)
        print(D)
    print(res)
    
if __name__=='__main__':
    hash()
