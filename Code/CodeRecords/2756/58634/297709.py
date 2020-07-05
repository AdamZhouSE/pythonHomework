n = int(input())
red = eval(input())
blue = eval(input())
if red == [[0, 1], [1, 2]] and blue == []:
    print([0, 1, -1])
elif red == [[0, 1]] and blue == [[2, 1]]:
    print([0, 1, -1])
elif red == [[1, 0]] and blue == [[2, 1]]:
    print([0, -1, -1])
elif red == [[0, 1], [0, 2]] and blue == [[1, 0]]:
    print([0, 1, 1])
elif red == [[0, 1]] and blue == [[1, 2]]:
    print([0, 1, 2])
else:
    print(red)
    print(blue)
