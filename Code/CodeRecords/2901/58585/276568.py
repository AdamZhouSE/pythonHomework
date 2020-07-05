def jud(n):
    n,a=divmod(n,2)
    while(n>0):
        n,b=divmod(n,2)
        if(a==b):
            return False
        a=b
    return True


n=int(input())
if(n==1):
    print("False")
else:
    if(jud(n)==True):
        print("True")
    else:
        print("False")