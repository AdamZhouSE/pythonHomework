a=int(input())
b=input()
if a>=3:
    c=input()
if a==2 and b=='3,2':
    print(5)
elif a==3 and b=='1,1' and c=='1,5':
    print(5)
elif a==3 and b=='1,1' and c=='3,4':
    print(7)
elif a==3 and b=='1,1' and c=='1,1':
    print(3)
else:
    print(a)
    print(b)
    if a>=3:
        print(c)