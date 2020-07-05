def coun(X,Y):
    X=int(X)
    Y=int(Y)
    i=0
    if X>Y:
        i=X-Y
        return i
    else:
        while X<Y:
            if Y%2==1:
                Y=Y+1
            else:
                Y=int(Y/2)
            i=i+1
        return i+X-Y
    

X=input()
Y=input()
i=coun(X,Y)
print(i)