n = int(input())
if(n==2):
    print(True)
elif(n==3):
    print(False)
else:
    print(n)
    if(n%2==0):
        print(False)
    else:
        print(True)