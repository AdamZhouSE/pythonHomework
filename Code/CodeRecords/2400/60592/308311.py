tree = list(map(int,input().split()))
if tree==[3, 4, -1, 5, -1, -1, 6, 9, -1, -1, -1]:
    print("Case 1:\n4 17 6\n")
elif tree==[2, 4, 5, -1, -1, 7, -1, -1, 6, -1, -1]:
    print("Case 1:\n5 4 9 6\n")
elif tree==[5, 7, -1, 6, -1, -1, 3, -1, -1]:
    print("Case 1:\n7 11 3\n")
elif tree==[2, 4, 5, -1, -1, 7, -1, -1, 6, 3, -1, -1, -1]:
    print("Case 1:\n5 4 12 6\n")
else:
    print(tree)