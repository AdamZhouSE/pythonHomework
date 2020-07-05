def isReverse(a):
    for i in range( int(len(a)/2)):
        if a[i]!=a[len(a)-i-1]:
            return False
    return True

a=input()
print(isReverse(a))