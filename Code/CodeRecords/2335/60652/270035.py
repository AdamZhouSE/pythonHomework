"""
和线性表有一题类似
"""
def min_operation(X,Y):
    if Y==X:
        return 0
    if Y<X:
        return X-Y
    if Y%2==0:
        return min_operation(X,Y//2)+1
    else:
        return min_operation(X,Y+1)+1

    
X=int(input())
Y=int(input())
print(min_operation(X,Y))