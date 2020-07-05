def hash():
    A=eval("["+input()+"]")
    B=eval("["+input()+"]")
    C=eval("["+input()+"]")
    D=eval("["+input()+"]")
    sumAB=[]
    res=0
    for a in A:
        for b in B:
                sumAB.append(a+b)

    sumAB.sort()
    for c in C:
        for d in D:
           while -(c+d) in sumAB:
               sumAB.remove(-(c+d))
               res+=1
    print(res)

if __name__=='__main__':
    hash()

