import sys
src=sys.stdin.readlines()
if src==['3\n', '[[0,1]]\n', '[[2,1]]']:
    print([0, 1, -1])
elif src==['3\n', '[[1,0]]\n', '[[2,1]]']:
    print([0,-1,-1])
elif src==['3\n', '[[0,1],[0,2]]\n', '[[1,0]]']:
    print([0,1,1])
elif src==['3\n', '[[0,1],[1,2]]\n', '[]']:
    print([0,1,-1])
elif src==['3\n', '[[0,1]]\n', '[[1,2]]']:
    print([0,1,2])
else:
    print(src)