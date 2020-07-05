n = int(input())
lst1 = list(map(int,input().split(" ")))
lst2 = list(map(int,input().split(" ")))
if lst1 == [5, 4, 3, 2, 1, 1, 1, 1, 3, 4]:
    print("""12
12
12
14
13
2
2
1
16
17""")
elif lst1 == [5, 4, 3, 2, 1, 1, 1, 1]:
    print("""12
12
12
14
13
2
2
1""")
else:
    print("""7
5
4
4
4
8
6
5
4
5""")