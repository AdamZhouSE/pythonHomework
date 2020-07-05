#Leercode 991 贪心算法
import re
def brokenCalc(X,Y):
    if (Y <= X):
        return X-Y;
    if (Y % 2 == 0):
        return 1 + brokenCalc(X, Y//2);
    else:
        return 1 + brokenCalc(X, Y+1);
m=re.findall('[0-9]',input())
X=int(m[0])
Y=int(m[1])
print(brokenCalc(X,Y))

