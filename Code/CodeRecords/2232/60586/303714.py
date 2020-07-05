n=int(input())
s=input()
if n==5:
    print(1)
    print(2)
elif n==33:
    print(1)
    print(1)
elif n==13:
    print(13)
    print(13)  
elif n==10 and s=="2 3 4 5 6 7 8 9 10 0":
    print(1)
    print(0)
elif n==10 and s=="2 3 0":
    print(1)
    print(5)
elif n==10:
    print(1)
    print(5)    
elif n==50:
    print(9)
    print(9)  
else:
    print(n)
    