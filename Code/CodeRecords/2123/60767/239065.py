def isSquare(num):
    for i in range(0,num):
        if(i*i==num):
            return True
        if(i*i>num):
            return False
num = int(input())
print(isSquare(num))