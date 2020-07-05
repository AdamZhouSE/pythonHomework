import math
s=input()
s=s[1:len(s)-1]
tree=s.split(",")
result=True
for i in range(len(tree)):
    if tree[i]!="null":
        tree[i]=int(tree[i])
for i in range(math.floor((len(tree)-1)/2)+1):
    if tree[i]!="null":
        left=2*i
        right=2*i+1
        if tree[left]!="null":
            if tree[left]>=tree[i]:
                result=False
                break
        if tree[right]!="null":
            if tree[right]<=tree[i]:
                result=False
                break
print(result)
