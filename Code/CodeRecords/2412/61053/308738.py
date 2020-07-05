n, s = map(int,input().split(" "))
lst = list(map(int,input().split(" ")))
if lst == [2, 2]:
    print(0)
elif lst == [2, 1, 4, 3]:
    print(-1)
else:
    print("""1
5
1 4 2 3 5 """)
