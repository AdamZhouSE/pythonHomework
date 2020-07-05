def isTwoPow(x):
    while True:
        if x<=0:
            return False
        if x==2 or x==1:
            return True
        if x>2:
            if x%2==0:
                x=x/2
            else:
                return False

print(isTwoPow(int(input())))