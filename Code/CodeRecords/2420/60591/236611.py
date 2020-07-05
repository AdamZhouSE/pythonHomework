def hasZero(string):
    if('0' in str(string)):
        return False
    else:
        return True

n = eval(input())
for x in range(1,n):
    if(hasZero(x)):
        if(hasZero(n-x)):
            print("[" + str(x) + ", " + str(n-x) + "]")
            break
