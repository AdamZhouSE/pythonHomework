def isThreePow(x):
    while True:
        if x<=0:
            return False
        if x==3 or x==1:
            return True
        if x==2:
            return False
        if x>3:
            if x%3==0:
                x=x/3
            else:
                return False

print(isThreePow(int(input())))