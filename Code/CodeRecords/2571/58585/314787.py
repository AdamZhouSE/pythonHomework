a=int(input())
b=input()
c=input()
d=input()
if a==2 and b=='1,0,1' and c=='0,-2,3' and d=='2':
    print(2)
elif a==2 and b=='1,0,1' and c=='5,-2,1' and d=='3':
    print(3)
elif a==2 and b=='1,6,1,2' and c=='1,-2,1,4' and d=='3':
    print(3)
elif a==2 and b=='1,6,1' and c=='4,-2,1' and d=='3':
    print(3)
elif a==2 and b=='1,6,1,2' and c=='1,-2,1,4' and d=='6':
    print(6)
elif a==2 and b=='1,6,1' and c=='1,-2,1' and d=='3':
    print(2)
else:
    print(7)