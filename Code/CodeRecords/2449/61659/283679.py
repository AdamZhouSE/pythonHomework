temp=list(input().split(","))
x=str(input())

if x in temp:
    print(temp.index(x))
else:
    print(-1)

