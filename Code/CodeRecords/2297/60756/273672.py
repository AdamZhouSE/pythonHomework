import math
n=int(input())
tree=list(input().split())
d=int(input())
L=int(pow(2,d-1)-1)
R=int(pow(2,d)-1)
if L>n:
    print("EMPTY")
else:
    if R<n:
        print(" ".join(tree[L:R]))
    else:
        print(" ".join(tree[L:]))