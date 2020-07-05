in1 = input().split(' ')
L = int(in1[0])
M = int(in1[1])

trees = [i for i in range(L+1)]
for i in range(M):
    in2 = input().split(' ')
    start = int(in2[0])
    end = int(in2[1])
    for j in range(start,end+1):
        try:
            trees.remove(j)
        except Exception:
            pass
print(len(trees))

