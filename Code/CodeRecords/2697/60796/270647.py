import math
s=input()
s=s[1:len(s)-1]
tree=s.split(",")
result="true"
for i in range(len(tree)):
    if tree[i]!="null":
        tree[i]=int(tree[i])
print(tree)
for i in range(math.floor((len(tree)-1)/2)+1):
    print(i)
    if tree[i]!="null":
        right=2*(i+1)
        left=right-1
        if tree[left]!="null":
            if tree[left]>=tree[i]:
                result="false"
                break
        if tree[right]!="null":
            if tree[right]<=tree[i]:
                result="false"
                break
print(result)
