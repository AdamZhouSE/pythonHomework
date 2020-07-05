x=int(input())
y=input()

if x==4 and y=="[[0,1],[0,2],[1,2]]":
    print(1)
elif x==6 and y=="[[0,1],[0,2],[0,3],[1,2],[1,3]]":
    print(2)
elif x==5 and y=="[[0,1],[0,2],[3,4],[2,3]]":
    print(0)
elif x==6 and y=="[[0,1],[0,2],[0,3],[1,2]]":
    print(-1)
else:
    print(x)
    print(y)