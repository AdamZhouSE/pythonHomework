n=int(input())
tree=input().split(" ")
d=int(input())
re=[]
if 2**(d-1)>n:
    print("EMPTY")
else:
    for i in range(2**(d-1)-1,2**d-1):
        if i<len(tree):
            re.append(tree[i])
    print(" ".join(re))