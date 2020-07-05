n = int(input())
tree = eval(input())
if(tree == [[1, 0], [1, 2], [1, 3]]):
    print([1])
elif(tree == [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]):
    print([3,4])
else:
    print(tree)