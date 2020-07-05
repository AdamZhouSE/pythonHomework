def compare(x,y):
    i=0
    while(i<len(x)):
        if(ord(x[i])>ord(y[i])):
            return True
        if(ord(x[i])<ord(y[i])):
            return False
        i+=1

a=input()
b=input()
c=input()
if(compare(a,b)==True):
    if(compare(a,c)==True):
        if(compare(b,c)==True):
            print(c)
            print(b)
            print(a)
        else:
            print(b)
            print(c)
            print(a)
    else:
        print(b)
        print(a)
        print(c)
else:
    if(compare(b,c)==True):
        if(compare(a,c)==True):
            print(c)
            print(a)
            print(b)
        else:
            print(a)
            print(c)
            print(b)
    else:
        print(c)
        print(b)
        print(a)