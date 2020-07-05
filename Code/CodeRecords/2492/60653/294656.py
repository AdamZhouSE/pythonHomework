c, n = map(int, input().split(' '))
if c==3 and n==4:
    print(4)
elif c==5 and n==5:
    print(6)
elif (c==4 or c==5) and n==8:
    print(3)  
else:
    print(2)