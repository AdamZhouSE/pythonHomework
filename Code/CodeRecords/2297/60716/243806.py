nodenum = int(input())
str = input().split(' ')
nodes = [int(i) for i in str]
level = int(input())
index=0
needsmin = 2**(level-1)-1
needsmax = 2**level-1
if needsmin>nodenum:
    print("EMPTY")
else:
    if needsmax>nodenum:
        needsmax=nodenum
    answer = list()
    for i in range(needsmin,needsmax):
        answer.append(nodes[i])
    strs = [str(i) for i in answer]
    answer = ' '.join(strs)
    print(answer)