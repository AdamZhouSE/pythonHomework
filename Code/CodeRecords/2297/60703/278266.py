n = int(input())
nodes = [int(x) for x in input().split()]
d = int(input())
#第i层第一个 2**i-1 从第0层开始
target = 2**(d-1)-1
targetEnd = min(len(nodes),2**d-1)
if(len(nodes)<target):
    print("EMPTY")
else:
    print(" ".join([str(x) for x in nodes[target:targetEnd]]))