#Leercode 991 贪心算法
import re
def brokenCalc(X,Y):
    if (Y <= X):
        return X-Y;
    if (Y % 2 == 0):
        return 1 + brokenCalc(X, Y//2);
    else:
        return 1 + brokenCalc(X, Y+1);
X=int(input())
Y=int(input())
print(brokenCalc(X,Y))