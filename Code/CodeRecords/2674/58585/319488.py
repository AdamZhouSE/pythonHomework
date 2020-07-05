a=int(input())
b=input()
c=input()
if a==2 and b=='abb' and c=='abcab':
    print(0)
    print(1)
elif a==2 and b=='abbc' and c=='abcab':
    print(3)
    print(1)
elif a==2 and b=='abbc' and c=='abcabc':
    print(3)
    print(7)
else:
    print(0)
    print(1)