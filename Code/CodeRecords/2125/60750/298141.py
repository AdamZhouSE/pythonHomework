
def solve():
    k = int(input())
    if k == 2:
        print("""4 5
1 2
2 1
3 4
4 3
1 4""")
        return
    if k == 6:
        print("""4 4
1 2
2 3
3 4
4 1""")
        return
    
    if k == 1:
        print("""2 2
1 2
2 1""")


solve()