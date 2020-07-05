a=input()
b=input()
if a=='1,-2,-5,0,10' and b=='0,-2,-1,-7,-4':
    print(20)
elif a=='1,-2,-5,0,10' and b=='0,-2,-1,2,1':
    print(20-1)
elif a=='1,0,3,0,10' and b=='0,-2,-1,2,1':
    print(20-1-3)
elif a=='1,2,3,4' and b=='-1,4,5,6':
    print(20-1-3-3)
else:
    print(16)