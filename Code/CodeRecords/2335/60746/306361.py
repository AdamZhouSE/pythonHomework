X=int(input())
Y=int(input())
def XtoY(X,Y):
    result=0
    while Y>X:
        result=result+1
        if Y%2!=0:
            Y=Y+1
        else:
            Y=int(Y/2)
    result=result+X-Y
    return result
print(XtoY(X,Y))