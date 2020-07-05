def hash():
    A=eval("["+input()+"]")
    B=eval("["+input()+"]")
    C=eval("["+input()+"]")
    D=eval("["+input()+"]")
    sumAB={}
    res=0
    for a in A:
        for b in B:
            if a+b in sumAB:
                sumAB[a+b]+=1
            else:
                sumAB[a+b]=1

    sumAB.sort()
    for c in C:
        for d in D:
           if -(c+d)in sumAB:
               res+=sumAB[a+b]
    print(res)

if __name__=='__main__':
    hash()
