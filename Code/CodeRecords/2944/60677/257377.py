expression=list(input())
left=0
right=0
for i in expression:
    if i=="(":
        left+=1
    else:
        right+=1
if left==right:
    print("YES",end="")
else:
    print("NO",end="")